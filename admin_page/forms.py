from django import forms
from blog.models import *

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('is_superuser','username','email','is_active','password')

	def clean_username(self):
		print('hana')
		username = self.cleaned_data['username'].lower()
		if User.objects.filter(username=username).exists():
			print('hana kman')
			raise forms.ValidationError('Username is already in use.')
		return username

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('category','image','title','content','slug','tagName')
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
