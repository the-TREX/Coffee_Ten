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
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['phone'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')

        return render(request, 'account/login.html', {'form': form})


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
