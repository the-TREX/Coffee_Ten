from math import trunc

from django.db.models import Sum
from django.shortcuts import render
from .models import Slider
from Products.models import Categories, Products


def index(request):
    X_slider = Slider.objects.all()
    categories = Categories.objects.all()
    bestsellers = Products.objects.filter(is_bestseller=True)
    featured_products = Products.objects.filter(is_offer=True)
    latest_products = Products.objects.order_by("-created_at")[:6]
    detail = Products.objects.all()
    context = {
        "slider": X_slider,
        "cat": categories,
        "bestsellers": bestsellers,
        "new_products": featured_products,
        "latest_products": latest_products,
        "detail": detail,
    }
    return render(request, "home/H_page.html", context)
