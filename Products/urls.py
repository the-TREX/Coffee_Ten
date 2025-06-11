from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('about/', views.About_us.as_view(), name='about'),
    path('shop/', views.All_Products.as_view(), name='shop'),
    path('category/<slug:slug>/', views.CategoryProductsView.as_view(), name='category_products'),
    path('<slug:slug>/', views.Detail_Product.as_view(), name='detail_products'),

]
