from django.shortcuts import render, HttpResponseRedirect
from posts.models import Post, Comments, reply, Category, Likes
# Create your views here.


def index(request):
    postList = Post.objects.all().order_by('created')
    postDic = {'posts': postList}
    return render(request, 'posts/post.html', context=postDic)
