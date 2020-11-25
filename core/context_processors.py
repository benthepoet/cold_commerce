from .models import Category, CartLine

def cart(request):
    cart = request.session.session_key

    if cart is None:
        cart_count = 0
    else:
        cart_count = CartLine.objects.filter(cart=cart).count()

    return {
        'cart_count': cart_count
        }

def categories(request):
    return {
        'all_categories': Category.objects.all()
        }