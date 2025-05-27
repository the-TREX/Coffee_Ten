from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('about/', views.about_us, name='about'),
    path('shop/', views.all_products, name='shop'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('<slug:slug>/', views.detail_products, name='detail_products'),

]
