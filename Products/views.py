from django.shortcuts import render, get_object_or_404
from .models import Categories, Products, Comment
from django.views.generic import ListView, TemplateView, DetailView, CreateView


class ProductListView(ListView):
    model = Products
    template_name = "products/templates/products/products_list.html"
    context_object_name = "prod"
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"
    context_object_name = "products"


class AboutusView(TemplateView):
    template_name = "products/about_us.html"


class CategoryProductsView(ListView):
    model = Products
    template_name = "products/category.html"
    context_object_name = "prod"
    paginate_by = 2  # تعداد محصولات در هر صفحه

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.category = get_object_or_404(Categories, slug=slug)
        return Products.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
