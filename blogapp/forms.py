from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BlogImageForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image']
