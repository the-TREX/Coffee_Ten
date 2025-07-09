from django.urls import path
from .views import OTPLoginView, OTPVerifyView

app_name = 'account'

urlpatterns = [
    path('login/', OTPLoginView.as_view(), name='login'),
    path('verify/', OTPVerifyView.as_view(), name='verify_otp'),
]
