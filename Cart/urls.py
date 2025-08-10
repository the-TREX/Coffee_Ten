from django.urls import path
from . import views
from .views import CartDetailView

app_name = 'Cart'
urlpatterns = [
    path('cart_detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
]
