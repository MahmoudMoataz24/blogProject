from django import forms
from blog.models import *
<<<<<<< HEAD

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_superuser','username','email','is_active')
		# widgets = {'is_superuser': forms.TextInput( attrs={'class': 'form-control'}),'username': forms.TextInput( attrs={'class': 'form-control'}),'email': forms.TextInput( attrs={'class': 'form-control'}),'is_active': forms.TextInput( attrs={'class': 'form-control'})}
=======
>>>>>>> develop

class UserForm(forms.ModelForm):
	class Meta:
<<<<<<< HEAD
		model=Post
		fields=('title','content','slug')

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=('title',)
=======
		model=User
		fields=('is_superuser','username','email','is_active')
		# widgets = {'is_superuser': forms.TextInput( attrs={'class': 'form-control'}),'username': forms.TextInput( attrs={'class': 'form-control'}),'email': forms.TextInput( attrs={'class': 'form-control'}),'is_active': forms.TextInput( attrs={'class': 'form-control'})}

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model=Post
# 		fields=('title',)
>>>>>>> develop
