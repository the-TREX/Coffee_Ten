from django.views.generic import *
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from Products.models import Products


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {"cart": cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Products, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        override_quantity = request.POST.get('override', 'false') == 'true'
        cart.add(product, quantity, override_quantity)
        return redirect('cart_detail')
