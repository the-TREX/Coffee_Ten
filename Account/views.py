from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, UserEditForm, ContactForm
from django.contrib import messages
from .models import *
from django.views.generic import FormView


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'account/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است'})
    else:
        return render(request, 'account/login.html')


def user_logout(request):
    logout(request)
    return redirect("/")


def user_edite(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما با موفقیت ویرایش شد.')
    return render(request, "account/edit.html", {'form': form})


# def contact_us(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "انتقاد شما با موفقیت ثبت گردید !")
#             return redirect("home:main")
#     else:
#         form = ContactForm()
#     return render(request, 'account/contact.html', {'form': form})

class ContactView(FormView):
    template_name = 'account/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data # یه دیکشنری شامل داده‌های فرم هست بعد از اعتبارسنجی
        Contact.objects.create(**form_data)
        return super().form_valid(form)
