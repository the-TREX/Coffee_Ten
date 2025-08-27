from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Contact
from django import forms
from django.core import validators
from Account.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'شماره موبایل یا ایمیل'}),
        label='',
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'رمز عبور'}),
        label='',
    )


class RegisterFormCustom(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'نام کاربری'}), label='')
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'ایمیل'}),
                             label='')
    phone = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'تلفن همراه'}), label='',
                            help_text='09...', validators=[validators.MaxLengthValidator(11)])
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'نام'}),
                                 label='')
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'نام خانوادگی'}),
                                label='')
    real_address = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'آدرس'}), label='')
    post_code = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'کد پستی'}), label='')

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input w-full', 'id': 'password', 'placeholder': 'رمز عبور'}),
        label=''
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input w-full', 'id': 'password', 'placeholder': ' تکرار رمز عبور'}),
        label=''
    )

    class Meta:
        model = User  # dare mige toye kodam model save she
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'real_address', 'post_code', 'password1',
                  'password2']

    # dare mige in filde ha ro dare

    def clean_username(self):  # baz nevisi filde username
        username = self.cleaned_data['username']  # meghdare filde ro migirim
        users = User.objects.filter(username=username)
        if users.exists():
            raise forms.ValidationError("این نام کاربری تکراری است و از قبل وجود دارد !")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل از قبل ثبت شده است!")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("این شماره از قبل ثبت شده است!")
        return phone


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
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "phone"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "phone", "is_active", "is_admin"]
