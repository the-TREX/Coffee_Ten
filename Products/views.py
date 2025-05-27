from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import Categories, Products


def detail_products(request, slug):
    products = get_object_or_404(Products, slug=slug)
    return render(request, "products/product_detail.html", context={"products": products, 'all_products': all_products})


def all_products(request):
    prod = Products.objects.all()
    return render(request, "products/products_list.html", context={"prod": prod})


def category_products(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    products = Products.objects.filter(category=category)
    categories = Categories.objects.all()
    return render(request, "products/category.html", {
        "category": category,
        "prod": products,
        "cat": categories,
    })
def about_us(request):
    return render(request, "products/about_us.html")
