from math import trunc

from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from .models import Slider
from Products.models import Categories, Products


def index(request):
    X_slider = Slider.objects.all()
    categories = Categories.objects.prefetch_related('products').all()
    bestsellers = Products.objects.filter(is_bestseller=True)
    latest_products = Products.objects.order_by("-created_at")[:4]
    detail = Products.objects.all()
    context = {
        "slider": X_slider,
        "category": categories,
        "bestsellers": bestsellers,
        "latest_products": latest_products,
        "detail": detail,

    }
    return render(request, "home/H_page.html", context)
