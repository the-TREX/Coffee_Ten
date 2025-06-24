from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'suggested', 'body']
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 4}),
        }
