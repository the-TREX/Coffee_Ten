from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, UpdateView, CreateView, View

from .forms import RegisterForm, UserEditForm, ContactForm, LoginForm
from .models import User, Contact


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    context_object_name = 'form'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()
        next_page = request.GET.get('next', '')
        return render(request, self.template_name, {'form': form, 'next': next_page})

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = request.POST.get('next', '')
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['phone'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect(next_page or '/')
            else:
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')
        return render(request, self.template_name, {'form': form, 'next': next_page})


def user_logout(request):
    logout(request)
    return redirect("/")


class UserEditeView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'account/edit.html'
    success_url = "/"


class ContactView(FormView):
    template_name = 'account/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        Contact.objects.create(**form.cleaned_data)
        return super().form_valid(form)
