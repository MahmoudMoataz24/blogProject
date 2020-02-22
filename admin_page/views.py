from django.shortcuts import render
from django.views import generic
from blog.models import Comments,Likes,Post,userAdds,reply,Category

# Create your views here.
class PostList(generic.ListView):
    queryset=Post.objects.filter(title='post').order_by('_created')
    template_name='user.html'

class PostDetail(generic.DetailView):
    model=Post
    template_name='post_details.html'