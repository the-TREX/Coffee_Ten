from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Categories, Products, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.urls import reverse, reverse_lazy


# from .forms import CommentForm

class ProductListView(ListView):
    model = Products
    template_name = "products/templates/products/products_list.html"
    context_object_name = "prod"
    paginate_by = 2


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"
    context_object_name = "products"


# class CommentProductListView(ListView):
#     model = Comment
#     template_name = "products/product_detail.html"
#     context_object_name = "comments"
#
#
#
# class CommentSaveView(CreateView):
#     model = Comment
#     template_name = "products/product_detail.html"
#     context_object_name = "message"
#     def form_valid(self, form):
#         form_data = form.cleaned_data
#         Comment.objects.create(**form_data)
#         return super(CommentSaveView, self).form_valid(form)


class AboutusView(TemplateView):
    template_name = "products/about_us.html"


class CategoryProductsView(ListView):
    model = Products
    template_name = "products/category.html"
    context_object_name = "prod"
    paginate_by = 2  # تعداد محصولات در هر صفحه

    def get_queryset(self):  # یه جورایی همون فلیتر ککنده data هست
        # گرفتن slug از url
        slug = self.kwargs.get('slug')
        # گرفتن دسته بندی مربوطه یا 404
        self.category = get_object_or_404(Categories, slug=slug)
        # فیلتر محصولات بر اساس دسته بندی
        return Products.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
