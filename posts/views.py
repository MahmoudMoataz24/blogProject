from django.shortcuts import render, HttpResponseRedirect
from posts.models import Post, Comments, reply, Category, Likes
# Create your views here.


def index(request):
    postList = Post.objects.all().order_by('created')
    postDic = {'posts': postList}
    return render(request, 'posts/post.html', context=postDic)


def showSinglePost(request, postID):
    post = Post.objects.get(id=postID)
    comments = Comments.objects.filter(postID_id=postID)
    cats = Category.objects.all()

    data = []
    for comment in comments:
        try:
            reply = Reply.objects.get(comId_id=comment.id)
            dic = {'comm': comment, 'rep': reply}
        except Exception as e:
            dic = {'comm': comment}
        finally:
            data.append(dic)
    context = {'post': post, 'data': data,
               'cats': cats, 'likeCount': likeCount}
    return render(request, 'posts/single.html', context)
