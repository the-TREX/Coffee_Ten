from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.core import validators
from django.core.exceptions import ValidationError

from .models import Contact, User


class LoginForm(forms.Form):
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'تلفن همراه'}),
        label='',
        help_text='09...',
        validators=[validators.MaxLengthValidator(11)]
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'رمز عبور'}),
        label=''
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'نام کاربری'}),
        label=''
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'ایمیل'}),
        label=''
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'تلفن همراه'}),
        label='',
        help_text='09...',
        validators=[validators.MaxLengthValidator(11)]
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'رمز عبور'}),
        label=''
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'تکرار رمز عبور'}),
        label=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("این نام کاربری تکراری است و از قبل وجود دارد !")
        return username


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'email', 'subject', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input1', 'placeholder': 'نام شما'}),
            'email': forms.EmailInput(attrs={'class': 'input1', 'placeholder': 'پست الکترونیک'}),
            'subject': forms.TextInput(attrs={'class': 'input1', 'placeholder': 'موضوع'}),
            'message': forms.Textarea(attrs={'class': 'input1', 'placeholder': 'متن پیام'}),
        }


class CustomUserCreationForm(forms.ModelForm):
    """برای ساخت کاربر جدید (ادمین پنل)"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "phone"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """فرم ویرایش کاربر (ادمین پنل)"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "phone", "is_active", "is_admin"]
