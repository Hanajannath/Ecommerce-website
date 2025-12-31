from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import*
from userapp.models import Cart,CartItem
from django.contrib import messages
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')

    order_details = []
    for order in orders:
        products = OrderProduct.objects.filter(order=order)
        order_details.append({
            'order': order,
            'products': products
        })

    return render(request, 'my_orders.html', {
        'order_details': order_details
    })


@staff_member_required
def manage_orders(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'manage_orders.html', {'orders': orders})

@staff_member_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.status = request.POST['status']
        order.save()
        return redirect('manage_orders')
    return render(request, 'update_order_status.html', {'order': order})

@staff_member_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('manage_orders')
# order_views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from adminapp.models import Product, Order, OrderProduct

@login_required
def place_order_direct(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Create order
    order = Order.objects.create(
        user=request.user,
        status='Pending'
    )

    # Attach product
    OrderProduct.objects.create(
        order=order,
        product=product,
        quantity=1
    )

    return redirect('my_orders')
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)

    if not cart.cart_items.exists():
        messages.error(request, "Your cart is empty")
        return redirect('view_cart')

    order = Order.objects.create(
        user=request.user,
        status='placed'
    )

    for item in cart.cart_items.all():
        OrderProduct.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    # Clear cart after order placed
    cart.cart_items.all().delete()

    return redirect('order_success')
# for one item
# @login_required
# def place_order(request, product_id):
#     # Get the product
#     product = Product.objects.get(id=product_id)

#     # Create a new order
#     order = Order.objects.create(
#         user=request.user,
#         status='placed'
#     )

#     # Add product to order
#     OrderProduct.objects.create(
#         order=order,
#         product=product,
#         quantity=1
#     )

#     return redirect('order_success')
@login_required
def order_success(request):
    return render(request, 'order_success.html')
# @login_required
# def my_orders(request):
#     # Get all orders for the logged-in user that are placed
#     orders = Order.objects.filter(user=request.user, status='placed').order_by('-order_date')

#     # For each order, fetch its products
#     order_details = []
#     for order in orders:
#         products = OrderProduct.objects.filter(order=order)
#         order_details.append({
#             'order': order,
#             'products': products
#         })