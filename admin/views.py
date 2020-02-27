from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

def showcatPosts(request,catID):
    posts=Post.objects.get(id=catID)
    context={'all_c':posts}
    return render(request,'admin/postview.html',context)

def liked(request,postid,postTitle):
    poste =Post.objects.get(id=postid)
    cuser=request.user.id
    like,created=Likes.objects.get_or_create(postID_id=postid,userID_id=cuser,isLiked=True)
    if(created==True):
        Likes.objects.filter(postID_id=postid,userID_id=cuser,isLiked=False).delete()

    return HttpResponseRedirect('/admin_page/postWhole.html'+postid)

def Intro(request):
    queryset = Post.objects.filter().order_by('-created')
    context = {'posts': queryset}
    return render(request, 'admin_page/Intro.html', context)

def forAdd(request):
    if request.method == "POST":
        forbidden_form = ForbiddenForm(request.POST, request.FILES)
        if forbidden_form.is_valid():
            forbidden_form.save()
        return HttpResponseRedirect("/admin/home/all")
    else:
        forbidden_form = ForbiddenForm()
        context = {'forbidden_form': forbidden_form}
        return render(request, 'admin_page/form.html', context)


def forAll(request):
    queryset = forbiddenWord.objects.filter()
    forr = forbiddenWord.objects.all()
    query = request.GET.get("q")
    qq = 'null'
    if query:
        qq = forbiddenWord.objects.filter(word=query)
        cont = {'all_words': qq}
        return render(request, 'admin_page/st_details.html', cont)
    else:
        context = {'all_words': forr}
        return render(request, 'admin_page/st_details.html', context)


def deleteFor(request, num):
    use = forbiddenWord.objects.get(id=num)
    use.delete()
    return HttpResponseRedirect('/admin/home/forAll')


def viewAll(request):
    queryset = User.objects.filter()
    users = User.objects.all()
    users_states=[]
    for user in users:
        i=0
        user_state = userState.objects.filter(user=user)
        state = user_state[i]
        users_states.append(str(state))
        i+=1
        # blocked = user_state.is_blocked
        # users_states.append(blocked)
    query = request.GET.get("q")
    qq = 'null'
    if query:
        users = User.objects.filter(username=query)
        cont = {'all': users, 'users_states':users_states}
        return render(request, 'admin_page/home.html', cont)
    else:
        context = {'all': users, 'users_states':users_states}
        return render(request, 'admin_page/home.html', context)


def addUser(request):
    user_form = UserForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
        return HttpResponseRedirect("/admin/home/all")
    context = {'user_form': user_form}
    return render(request, 'admin_page/st_add.html', context)


def EditUser(request, num):
    user = User.objects.get(id=num)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/admin/home/all")
    else:
        user_form = UserForm(instance=user)
        context = {'user_form': user_form}
        return render(request, 'admin_page/st_add.html', context)


def deleteUser(request, num):
    user = User.objects.get(id=num)
    user.delete()
    return HttpResponseRedirect('/admin/home/all')


def PostList(request):
    user = request.user
    user_state = userState.objects.get(user=user)
    is_blocked = user_state.is_blocked
    queryset = Post.objects.filter().order_by('-created')
    cat = Category.objects.all()
    query = request.GET.get("q")
    qq = 'null'
    if not is_blocked:
        if query:
            qq = Post.objects.filter(title=query)
            cont = {'all_cat': cat, 'object_list': qq}
            return render(request, 'admin_page/post_detail.html', cont)
        else:
            context = {'all_cat': cat, 'post_list': queryset, 'is_blocked':is_blocked}
            return render(request, 'admin_page/admin_home.html', context)
    else:
        messages.error(request, 'Sorry you are blocked contact the admin')
        return redirect('login')


def post_details(request, post_id):
    all_cat = Category.objects.all()
    postt = Post.objects.get(id=post_id)
    # user=User.objects.get(id=)
    # all_Tags=Tag.objects.all()
    print(postt)
    comments = Comments.objects.filter(id=postt.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # new_comment.author=user
            new_comment.postID = postt
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'admin_page/postWhole.html', {'posting': postt,
                                                         'comments': comments,
                                                         'new_comment': new_comment,
                                                         'comment_form': comment_form})


def like_post(request, post_title):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect('/' + post_title)


def viewPost(request):
    all_posts = Post.objects.all()
    queryset = Post.objects.filter()
    query = request.GET.get("q")
    qq = 'null'
    if query:
        pos = Post.objects.filter(title=query)
        cont = {'all_posts': pos}
        return render(request, 'admin_page/posts.html', cont)
    else:
        context = {'all_posts': all_posts}
        return render(request, 'admin_page/posts.html', context)


def addPost(request):
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
        post_form.save()
        return HttpResponseRedirect("/admin/home/posts")
    context = {'post_form': post_form}
    return render(request, 'admin_page/post_add.html', context)


def EditPost(request, num):
    post = Post.objects.get(id=num)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin/home/posts')
    else:
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'admin_page/post_add.html', context)


def delPost(request, num):
    post = Post.objects.get(id=num)
    post.delete()
    return HttpResponseRedirect('/admin/home/posts')


def catAll(request):
    all_cat = Category.objects.all()
    queryset = Category.objects.filter()
    query = request.GET.get("q")
    qq = 'null'
    if query:
        cat = Category.objects.filter(title=query)
        cont = {'all_cat': cat}
        return render(request, 'admin_page/category.html', cont)
    else:
        context = {'all_cat': all_cat}
        return render(request, 'admin_page/category.html', context)


def catEdit(request, num):
    cat_obj = Category.objects.get(id=num)
    if (request.method == "POST"):
        cat_form = CategoryForm(request.POST, instance=cat_obj)
        if cat_form.is_valid():
            cat_form.save()
        return HttpResponseRedirect("/admin/home/catAll")
    else:
        cat_form = CategoryForm(instance=cat_obj)
        context = {'cat_form': cat_form}
        return render(request, 'admin_page/cat_add.html', context)


def catDel(request, num):
    cat_obj = Category.objects.get(id=num)
    cat_obj.delete()
    return HttpResponseRedirect("/admin/home/catAll")


def catAdd(request):
    if request.method == "POST":
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
        return HttpResponseRedirect("/admin/home/catAll")
    else:
        cat_form = CategoryForm()
        context = {
            'cat_form': cat_form,
            'title': 'Add'
        }
        return render(request, "admin_page/cat_add.html", context)
