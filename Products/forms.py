from django import forms

from Products.models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('suggested', 'title', 'body')
#         widgets = {
#             'title': forms.CharField(label='Title', max_length=100),
#             'body': forms.CharField(widget=forms.Textarea),
#             'suggested': forms.BooleanField(required=False)
#         }
