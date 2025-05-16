from django.shortcuts import render
from .models import Categories , Products


def category(request):
    cat = Categories.objects.all()
    best = Products.objects.all()
    return render(request, 'products/categories.html' , {'cat':cat , 'best':best})

def bestsellers(request):
    best = Products.objects.all()
    return render(request , 'products/categories.html' , {'best':best})