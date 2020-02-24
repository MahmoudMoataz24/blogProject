from blog.models import *
from user.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


def viewPost(request):
    post = Post.objects.all()
    context = {'all' : post }
    return render(request,'user_page/home.html', context) 


# def viewPost(request): #slug):
#     template_name = 'user_page/home.html'
#     # post = get_object_or_404(Post, slug=slug)
#     post = Post.objects.all()
#     # comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                         #    'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})