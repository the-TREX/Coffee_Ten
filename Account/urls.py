from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit_profile/<int:pk>', views.UserEditeView.as_view(), name='edit_profile'),
    path('contact_us/', views.ContactView.as_view(), name='contact_us'),
]