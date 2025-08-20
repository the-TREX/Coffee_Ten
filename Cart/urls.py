from django.urls import path
from . import views
from .views import CartDetailView, CartUpdateView, OrderCreationView

app_name = 'Cart'
urlpatterns = [
    path('cart_detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<str:id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path("update/<int:product_id>/", CartUpdateView.as_view(), name="cart_update"),
    path("order/", OrderCreationView.as_view(), name="cart_order_detail"),
]
