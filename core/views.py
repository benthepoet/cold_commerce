from django.shortcuts import render

from .forms import ProductVariantForm
from .models import Cart, CartLine, Category, Product, ProductVariant

def index(request):
    return render(request, 'core/index.html')

def cart(request):
    cart = request.session.session_key

    if cart is None:
        cartlines = []
    else:
        cartlines = CartLine.objects.filter(cart=cart)

    context = {
        'cartlines': cartlines
    }

    return render(request, 'core/cart.html', context)

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
        }

    return render(request, 'core/category.html', context)

def product(request, product_id, category_id):
    if request.method == 'POST':
        form = ProductVariantForm(request.POST)
        if form.is_valid():
            if request.session.session_key is None:
                request.session.create()

            try:
                cart = Cart.objects.get(pk=request.session.session_key)
            except Cart.DoesNotExist:
                cart = Cart(id=request.session.session_key)
                cart.save()

            product_variant = form.cleaned_data['product_variant']
            quantity = form.cleaned_data['quantity']

            try:
                cart_line = CartLine.objects.get(cart=cart, product_variant=product_variant)
                cart_line.quantity += quantity
            except CartLine.DoesNotExist:
                cart_line = CartLine(cart=cart, product_variant=ProductVariant(id=product_variant), quantity=quantity)

            cart_line.save()

    product = Product.objects.get(pk=product_id)
    variants = ProductVariant.objects.filter(product=product)
    context = {
        'product': product, 
        'variants': variants
        }

    return render(request, 'core/product.html', context)