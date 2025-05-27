from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'نام کاربری'}), label='')
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'ایمیل'}),
                             label='')
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'رمز عبور'}),
                                label='')
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'تکرار رمز عبور'}),
                                label='')

    class Meta:
        model = User  # dare mige toye kodam model save she
        fields = ['username', 'email', 'password1', 'password2']  # dare mige in filde ha ro dare

    def clean_username(self):  # baz nevisi filde username
        username = self.cleaned_data['username']  # meghdare filde ro migirim
        users = User.objects.filter(username=username)
        if users.exists():
            raise forms.ValidationError("این نام کاربری تکراری است و از قبل وجود دارد !")
        return username


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


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
