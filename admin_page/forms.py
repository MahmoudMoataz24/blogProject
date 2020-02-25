from django import forms
from blog.models import *

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_superuser','username','email','is_active','password')
		# widgets = {'is_superuser': forms.TextInput( attrs={'class': 'form-control'}),'username': forms.TextInput( attrs={'class': 'form-control'}),'email': forms.TextInput( attrs={'class': 'form-control'}),'is_active': forms.TextInput( attrs={'class': 'form-control'})}

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('category','title','content','slug')

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=('title',)
