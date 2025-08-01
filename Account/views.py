from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PhoneForm, OTPForm
from .models import OTP, User
from .utils import generate_otp, send_otp_sms


class OTPLoginView(View):
    template_name = 'account/login.html'

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
