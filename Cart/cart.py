from decimal import Decimal

from rest_framework.templatetags.rest_framework import items

from Products.models import Products

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product.id,
                'quantity': 0,
                'price': str(product.price),
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id]['quantity'] += int(quantity)

        if self.cart[product_id]['quantity'] <= 0:
            self.remove(product_id)
        else:
            self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            item['product'] = Products.objects.get(id=int(item['product_id']))
            price = Decimal(item['price'])
            if item['product'].get_discount_price() > 0:
                discount_price = item['product'].get_discount_price()
                item['total'] = Decimal(discount_price) * int(item['quantity'])
            else:
                item['total'] = price * int(item['quantity'])
            item['id'] = item['product_id']
            yield item

    def total(self):
        cart = self.cart.values()
        total = 0
        for item in cart:
            total += item['total']
        return total

    def delete_cart(self):
        del self.session[CART_SESSION_ID]

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
# from Products.models import Products
# from decimal import Decimal, InvalidOperation
#
# CART_SESSION_ID = 'cart'
#
#
# class Cart:
#     def __init__(self, request):  # -----OK-----
#         self.session = request.session
#         cart = self.session.get(CART_SESSION_ID)  # etelat sabadkharid
#         if not cart:
#             cart = self.session[CART_SESSION_ID] = {}
#         self.cart = cart
#
#     # Add product to cart
#     def add(self, product, quantity=1):
#         product_id = str(product.id)  # Get product id
#         if product_id not in self.cart:  # age maosol dar cart nabod misazimesh
#             self.cart[product_id] = {
#                 'product_id': product.id,
#                 'quantity': int(quantity),
#                 'price': str(product.price),
#             }
#         self.cart[product_id]['quantity'] = int(quantity)
#         self.save()
#
#     def save(self):
#         self.session.modified = True
#
#     def __iter__(self):
#         cart = self.cart.copy()
#         for item in cart.values():
#             item['product'] = Products.objects.get(id=int(item['product_id']))
#             item['total'] = int(item['price']) * int(item['quantity'])
#             yield item
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # def add(self, product, quantity=1):
#     #     product_id = str(product.id)
#     #     if product_id not in self.cart:
#     #         self.cart[product_id] = {
#     #             'quantity': 0,
#     #             'price': str(product.price),
#     #         }
#     #     self.cart[product_id]['quantity'] = int(quantity)
#     #     self.save()
#     #
#     # def __iter__(self):
#     #     cart = self.cart.copy()
#     #     for item in cart.values():
#     #         item['product'] = Products.objects.get(id=item['product_id'])
#     #         item['total'] = int(item['price'] * item['quantity'])
#     #         yield item
