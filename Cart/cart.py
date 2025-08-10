from Products.models import Products
from decimal import Decimal

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    # Add product to cart
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)  # Get product id

        if product_id not in self.cart:  # age maosol dar cart nabod misazimesh
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)
        for product in products:
            cart_item = self.cart[str(product.id)]
            cart_item['product'] = product
            cart_item['total_price'] = Decimal(cart_item['price']) * (cart_item['quantity'])
            yield cart_item
