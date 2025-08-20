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


<<<<<<< HEAD
class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        next_page = request.GET.get('next', '')
        return render(request, 'account/login.html', {'form': form, 'next': next_page})

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = request.POST.get('next', '')
=======
class UserLoginView(View):  # OK
>>>>>>> Try_To_MakeBetter_Account_App
    def get(self, request):
        form = PhoneForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PhoneForm(request.POST)
>>>>>>> d5b69549689337c2da335bf34d0b440626b39ab0
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
                return redirect(next_page or '/')  # اگر next نبود برو صفحه اصلی
            else:
<<<<<<< HEAD
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')

        return render(request, 'account/login.html', {'form': form, 'next': next_page})


def user_logout(request):
    logout(request)
    return redirect("/")


class UserEditeView(UpdateView):  # OK
    model = User
    fields = ['username', 'email']
    template_name = 'account/edit.html'
    success_url = "/"


class ContactView(FormView):  # OK
    template_name = 'account/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data  # یه دیکشنری شامل داده‌های فرم هست بعد از اعتبارسنجی
        Contact.objects.create(**form_data)
        return super().form_valid(form)
=======
                form.add_error('code', 'کد وارد شده نادرست یا منقضی شده است')
        return render(request, self.template_name, {'form': form})
>>>>>>> d5b69549689337c2da335bf34d0b440626b39ab0
