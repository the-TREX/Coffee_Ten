from django.views.generic import *
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from Products.models import Products
from .models import Order, OrderItem


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Products, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart.add(product, quantity)
        return redirect('Cart:cart_detail')


class CartRemoveView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove(id)
        return redirect('Cart:cart_detail')


class CartUpdateView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Products, id=product_id)

        action = request.POST.get("action")

        if action == "increment":
            cart.add(product, quantity=1, override_quantity=False)

        elif action == "decrement":
            cart.add(product, quantity=-1, override_quantity=False)

        else:
            quantity = int(request.POST.get("quantity", 1))
            cart.add(product, quantity=quantity, override_quantity=True)

        return redirect("Cart:cart_detail")

class OrderDetailView(View):
    def get(self, request, product_id):
        order = get_object_or_404(Order, id=product_id)
        return render(request , 'cart/order_detail.html', {'order': order})

class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'],
                                     price=int(float(item['price'])))
        cart.delete_cart()
        return redirect('Cart:cart_order_detail')
