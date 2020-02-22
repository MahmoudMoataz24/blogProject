from django import forms
from blog.models import Comments,Likes,Post,userAdds,reply,Category

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','image','content','user_id')
		widgets = {
		'title' : forms.TextInput(attrs={'class':'form-control'}),
		'image' : forms.FileInput(attrs={'class':'form-control-image'}),
		'content' : forms.TextInput(attrs={'class':'form-control'}),
		}