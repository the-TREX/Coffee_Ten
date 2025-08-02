from django.views import View
from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login
from .forms import PhoneForm, OTPForm
from .models import OTP, User
from .utils import generate_otp, send_otp_sms


class OTPLoginView(View):
    template_name = 'account/login.html'

=======
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterFormCustom, UserEditForm, ContactForm, LoginForm
from django.contrib import messages
from .models import *
from django.views.generic import FormView, UpdateView, CreateView, View
from .models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout


class UserRegisterView(CreateView):
    form_class = RegisterFormCustom
    template_name = 'account/register.html'
    context_object_name = 'form'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'],
                                       email=form.cleaned_data['email'],
                                       phone=form.cleaned_data['phone'],
                                       first_name=form.cleaned_data['first_name'],
                                       last_name=form.cleaned_data['last_name'],
                                       real_address=form.cleaned_data['real_address'],
                                       post_code=form.cleaned_data['post_code'],
                                       password=form.cleaned_data['password1'], )
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})


class UserLoginView(View):  # OK
>>>>>>> Try_To_MakeBetter_Account_App
    def get(self, request):
        form = PhoneForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            code = generate_otp()
            OTP.objects.create(phone=phone, code=code)
            send_otp_sms(phone, code)
            request.session['phone'] = phone
            return redirect('otp_auth:verify_otp')
        return render(request, self.template_name, {'form': form})


class OTPVerifyView(View):
    template_name = 'account/verify.html'

    def get(self, request):
        if not request.session.get('phone'):
            return redirect('account:login')
        form = OTPForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        phone = request.session.get('phone')
        form = OTPForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            otp = OTP.objects.filter(phone=phone, code=code).last()
            if otp and otp.is_valid():
                user, _ = User.objects.get_or_create(
                    phone=phone,
                    defaults={
                        'username': phone,
                        'email': f'{phone}@example.com'
                    }
                )
                login(request, user)
                return redirect('/')
            else:
                form.add_error('code', 'کد وارد شده نادرست یا منقضی شده است')
        return render(request, self.template_name, {'form': form})
