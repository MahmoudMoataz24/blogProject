from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_superuser','username','email','is_active')

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username is already in use.')
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email is already in use.')
		return email

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('category','image','title','content','slug','tagName')
	def clean_image(self):
            image = self.cleaned_data.get('image', False)
            if image:
                if image._height > 1920 or image._width > 1080:
                    raise ValidationError("Height or Width is larger than what is allowed")
                return image
            else:
                raise ValidationError("No image found")
	# def cleaned_data(self):
	# 	if('image' in request.FILES):
	# 		image = request.FILES['image']
	# 	if image:
	# 		if image._size:
	# 			if image:
	# 				if image._size > 1*1024*1024:
	# 					raise ValidationError("Image file too large ( > 4mb )")
	# 			else:
	# 				raise ValidationError("Couldn't read uploaded image")
	# 		else:
	# 			raise ValidationError("image format should be .png %s"%(image_format))
	# 		return image

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=('title',)

class ForbiddenForm(forms.ModelForm):
	class Meta:
		model = forbiddenWord
		fields = ('word',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'content')