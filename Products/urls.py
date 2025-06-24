from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('shop/', views.ProductListView.as_view(), name='shop'),
    path('category/<slug:slug>/', views.CategoryProductsView.as_view(), name='category_products'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail_products'),

]
