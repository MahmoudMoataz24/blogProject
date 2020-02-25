from blog.models import *
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('userID', 'postID', 'content')

        