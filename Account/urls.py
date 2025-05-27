from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/', views.user_edite, name='edit_profile'),
    path('contact_us/', views.contact_us, name='contact_us'),
]