from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, UserEditForm, ContactForm, LoginForm
from django.contrib import messages
from .models import *
from django.views.generic import FormView, UpdateView, CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
=======
<<<<<<< HEAD
from django.contrib.auth import login
from .forms import PhoneForm, OTPForm
from .models import OTP, User
from .utils import generate_otp, send_otp_sms
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    context_object_name = 'form'
    success_url = '/'

<<<<<<< HEAD


class UserLoginView(View):  # OK
=======
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
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
<<<<<<< HEAD
        form = LoginForm(request.POST)
=======
        form = PhoneForm(request.POST)
>>>>>>> d5b69549689337c2da335bf34d0b440626b39ab0
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['phone'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(next_page or '/')  # اگر next نبود برو صفحه اصلی
            else:
<<<<<<< HEAD
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')

        return render(request, 'account/login.html', {'form': form})
=======
<<<<<<< HEAD
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')

        return render(request, 'account/login.html', {'form': form, 'next': next_page})
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab


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
<<<<<<< HEAD
=======
=======
                form.add_error('code', 'کد وارد شده نادرست یا منقضی شده است')
        return render(request, self.template_name, {'form': form})
>>>>>>> d5b69549689337c2da335bf34d0b440626b39ab0
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
