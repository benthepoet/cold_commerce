from django.shortcuts import render

from .forms import ProductVariantForm
from .models import Cart, CartLine, Product, ProductVariant

def index(request):
    return render(request, 'core/index.html')

def product(request, id, category_id):
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

            cart_line = CartLine(cart=cart, product_variant=ProductVariant(id=product_variant), quantity=quantity)
            cart_line.save()

    product = Product.objects.get(pk=id)
    variants = ProductVariant.objects.filter(product=id)
    context = {
        'product': product, 
        'variants': variants
        }

    return render(request, 'core/product.html', context)