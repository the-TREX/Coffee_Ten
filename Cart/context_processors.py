from .cart import Cart

def cart(request):
    return {
        'cart': request.session.get('cart', {})
    }


