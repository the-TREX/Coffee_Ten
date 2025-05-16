from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('categories', views.category, name='categories'),
    path('bestsellers', views.bestsellers, name='bestsellers'),
]