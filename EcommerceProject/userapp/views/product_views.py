from django.shortcuts import render,redirect, get_object_or_404
from adminapp.models import*
from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        stock = request.POST['stock']
        image = request.FILES.get('image')
        Product.objects.create(name=name, price=price, description=description, stock=stock, image=image)
        return redirect('product_list')
    return render(request, 'create_product.html')

@staff_member_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.stock = request.POST['stock']
        if request.FILES.get('image'):
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')
    return render(request, 'update_product.html', {'product': product})

@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')

@staff_member_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def userproducts(request):
    products=Product.objects.all()
    return render(request,'cards.html',{'products':products})
# def welcome(request):
#     return render(request,'welcome.html')
# def home(request):
#     return render(request,'home.html')
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    viewed = request.session.get('recently_viewed', [])

    if product_id not in viewed:
        viewed.insert(0, product_id)

    request.session['recently_viewed'] = viewed[:5]

    return render(request, 'product_detail.html', {'product': product})
def recently_viewed(request):
    ids = request.session.get('recently_viewed', [])
    products = Product.objects.filter(id__in=ids)
    return render(request, 'recent.html', {'products': products})
