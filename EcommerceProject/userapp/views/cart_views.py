from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import*
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userapp.models import Cart, CartItem
# @login_required
# session based
# def add_to_cart(request, product_id):
#     # Make sure product exists
#     product = get_object_or_404(Product, id=product_id)
    
#     # request.user is already a User instance because of @login_required
#     cart = request.session.get('cart', {})
#     if str(product.id) in cart:
#         cart[str(product.id)] += 1
#     else:
#         cart[str(product.id)] = 1
    
#     request.session['cart'] = cart
#     return redirect('view_cart')
# database based
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 1))
    if quantity <= 0:
        messages.error(request, "Invalid quantity")
        return redirect("cards")

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    messages.success(request, "Product added to cart")
    return redirect("view_cart")

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart")
    return redirect("view_cart")

# session based
# @login_required
# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     cart.pop(str(product_id), None)
#     request.session['cart'] = cart
#     return redirect('view_cart')

# session
# @login_required
# def view_cart(request):
#     cart = request.session.get('cart', {})
#     products = []
#     total = 0
#     for product_id, qty in cart.items():
#         product = Product.objects.get(id=product_id)
#         product.qty = qty
#         product.subtotal = qty * product.price
#         total += product.subtotal
#         products.append(product)
    # return render(request, 'cart.html', {'products': products, 'total': total})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart2.html", {"cart": cart})
@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    quantity = int(request.POST.get("quantity", 1))
    if quantity <= 0:
        cart_item.delete()
        messages.info(request, "Item removed from cart")
    else:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, "Cart updated")

    return redirect("view_cart")

# @login_required
# def checkout(request):
#     cart = request.session.get('cart', {})
#     products = []
#     total = 0

#     for product_id, qty in cart.items():
#         product = Product.objects.get(id=product_id)
#         product.qty = qty
#         product.subtotal = product.price * qty
#         total += product.subtotal
#         products.append(product)

#     return render(request, 'checkout.html', {
#         'products': products,
#         'total': total
#     })
# from django.utils import timezone
# @login_required
# def place_cart_order(request):
#     cart = request.session.get('cart', {})

#     if not cart:
#         return redirect('view_cart')

#     order = Order.objects.create(
#         user=request.user,
#         status='Placed',
#         order_date=timezone.now()
    
#     )

#     for product_id, qty in cart.items():
#         product = Product.objects.get(id=product_id)
#         OrderProduct.objects.create(
#             order=order,
#             product=product,
#             quantity=qty
#         )

#     # Clear cart after placing order
#     request.session['cart'] = {}

#     return redirect('my_orders')

