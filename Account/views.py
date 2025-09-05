from django.shortcuts import render, redirect
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
            # ساخت کاربر
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                real_address=form.cleaned_data['real_address'],
                post_code=form.cleaned_data['post_code'],
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],  # شماره یا ایمیل را وارد کنید
                password=form.cleaned_data['password1']
            )
            if user is not None:
                login(request, user)
                return redirect('/')
            # authenticate با backend جدید

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    template_name = 'account/login.html'

    def get_next_url(self, request):
        return request.POST.get('next') or request.GET.get('next', '')

    def get(self, request):
        form = LoginForm()
        next_url = self.get_next_url(request)
        return render(request, self.template_name, {'form': form, 'next': next_url})

    def post(self, request):
        form = LoginForm(request.POST)
        next_url = self.get_next_url(request)
        remember_me = request.POST.get('remember_me', None)
        if form.is_valid():
            # authenticate با شماره یا ایمیل
            user = authenticate(
                username=form.cleaned_data['username'],  # شماره یا ایمیل
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)
                else:
                    request.session.set_expiry(0)
                return redirect(next_url or '/')
            else:
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')

        return render(request, self.template_name, {'form': form, 'next': next_url})


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
