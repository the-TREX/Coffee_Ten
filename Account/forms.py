from django import forms

class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=15)

class OTPForm(forms.Form):
    code = forms.CharField(max_length=6)
