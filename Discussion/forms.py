from django.forms import ModelForm
from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'attachment')


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('title', 'body', 'attachment')

        widgets = {
            'body': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Reply',
                }
            ),
        }
