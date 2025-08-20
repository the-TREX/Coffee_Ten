from django.views.generic import ListView, TemplateView, DetailView, CreateView, View
from .forms import *
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Comment
from .forms import CommentForm
from django.utils import timezone


class ProductListView(ListView):
    model = Products
    template_name = "products/templates/products/products_list.html"
    context_object_name = "prod"
    paginate_by = 8

    # --- Filter Products ---
    def get_queryset(self):
        queryset = super().get_queryset()  # == Products.objects.all()
        sort = self.request.GET.get('sort', 'is_bestseller')

        if sort == 'popular':
            queryset = queryset.order_by('-rating')
        elif sort == 'is_bestseller':
            queryset = queryset.order_by('-is_bestseller')
        elif sort == 'cheapest':
            queryset = queryset.order_by('price')
        elif sort == 'expensive':
            queryset = queryset.order_by('-price')

        return queryset


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        comments = product.comments.all().order_by('-created_at')
        form = CommentForm()
        return render(request, 'products/product_detail.html', {
            'products': product,
            'comments': comments,
            'form': form
        })

    def post(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.created_at = timezone.now()
            comment.save()
            return redirect('products:detail_products', slug=slug)
        comments = product.comments.all().order_by('-created_at')
        return render(request, 'products/product_detail.html', {
            'products': product,
            'comments': comments,
            'form': form
        })


class AboutUsView(TemplateView):
    template_name = "products/about_us.html"


class CategoryProductsView(ListView):
    model = Products
    template_name = "products/category.html"
    context_object_name = "prod"
    paginate_by = 8  # تعداد محصولات در هر صفحه

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.category = get_object_or_404(Categories, slug=slug)

        queryset = Products.objects.filter(category=self.category)

        sort = self.request.GET.get('sort', 'is_bestseller')

        if sort == 'created_at':
            queryset = queryset.order_by('-created_at')
        elif sort == 'is_bestseller':
            queryset = queryset.order_by('-is_bestseller')
        elif sort == 'cheapest':
            queryset = queryset.order_by('price')
        elif sort == 'expensive':
            queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
