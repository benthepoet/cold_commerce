from django.shortcuts import render

from .models import Product, ProductVariant

def index(request):
    return render(request, 'core/index.html')

def product(request, id, category_id):
    product = Product.objects.get(pk=id)
    variants = ProductVariant.objects.filter(product=id)
    context = {
        'product': product, 
        'variants': variants
        }
    return render(request, 'core/product.html', context)