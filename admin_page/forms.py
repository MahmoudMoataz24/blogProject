from django import forms
from blog.models import *
from posts.models import *

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_superuser', 'username', 'email', 'is_active')
        # widgets = {'is_superuser': forms.TextInput( attrs={'class': 'form-control'}),'username': forms.TextInput( attrs={'class': 'form-control'}),'email': forms.TextInput( attrs={'class': 'form-control'}),'is_active': forms.TextInput( attrs={'class': 'form-control'})}


class UserForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'slug')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
