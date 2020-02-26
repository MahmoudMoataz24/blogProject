from django.shortcuts import render
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from admin_page.forms import UserForm,PostForm,CategoryForm,ForbiddenForm
# from django.db.models import Q
def Intro(request):
	queryset = Post.objects.filter().order_by('-created')
	context={'posts':queryset}
	return render(request,'admin_page/Intro.html',context)

def forAdd(request):
	if request.method == "POST":
		forbidden_form = ForbiddenForm(request.POST,request.FILES)
		if forbidden_form.is_valid():
			forbidden_form.save()
		return HttpResponseRedirect("/admin_page/home/all")
	else:
		forbidden_form =ForbiddenForm() 
		context = {'forbidden_form':forbidden_form}
		return render(request,'admin_page/form.html',context)

def forAll(request):
	forr=forbiddenWord.objects.all()
	context ={'all_words' : forr}
	return render(request,'admin_page/st_details.html',context)

def deleteFor(request,num):
	use = forbiddenWord.objects.get(id = num)
	use.delete()
	return HttpResponseRedirect('/admin_page/home/forAll')

def viewAll(request):
	user=User.objects.all()
	print(user)
	context ={'all' : user}
	return render(request,'admin_page/home.html',context)

def addUser(request):
	user_form = UserForm(request.POST or None)
	if user_form.is_valid():
		user_form.save()
		return HttpResponseRedirect("/admin_page/home/all")
	context = {'user_form':user_form}
	return render(request,'admin_page/st_add.html',context)

def EditUser(request,num):
	user=User.objects.get(id = num)
	if request.method=="POST":
		user_form=UserForm(request.POST,instance=user)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect("/admin_page/home/all")
	else:
		user_form=UserForm(instance=user)
		context={'user_form':user_form}
		return render(request,'admin_page/st_add.html',context)

def deleteUser(request,num):
	user = User.objects.get(id = num)
	user.delete()
	return HttpResponseRedirect('/admin_page/home/all')

def PostList(request):
	queryset = Post.objects.filter().order_by('-created')
	cat = Category.objects.all()
	query = request.GET.get("q")
	qq='null'
	if query:
		qq = Post.objects.filter(title=query)
		cont={'all_cat' : cat,'object_list' : qq}
		return render(request,'admin_page/post_detail.html',cont)
	else:
		context = {'all_cat' : cat , 'post_list' : queryset}
		return render(request,'admin_page/admin_home.html',context)

# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
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
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})

def like_post(request, post_title):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect('/'+post_title)


# def searchForPost(request):
# 	print('ana hana')
# 	query = request.GET.get("q")
# 	print(query)
# 	if query:
# 		q = Post.objects.filter(title=query)
# 		# print(q)
# 		context = {'object_list' : q}
# 		return render(request,'admin_page/post_detail.html',context)

def viewPost(request):
	all_posts = Post.objects.all()
	print(all_posts)
	context = {'all_posts':all_posts}
	return render(request,'admin_page/posts.html',context)

def addPost(request):
	if request.method == "POST":
		post_form = PostForm(request.POST,request.FILES)
		if post_form.is_valid():
			post_form.save()
		return HttpResponseRedirect("/admin_page/home/posts")
	else:
		post_form =PostForm() 
		context = {'post_form':post_form}
		return render(request,'admin_page/post_add.html',context)

def EditPost(request,num):
	post = Post.objects.get(id=num)
	if request.method=="POST":
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('admin_page/home/posts')
	else:
		form = PostForm(instance=post)
		context ={'form':form}
		return render(request,'admin_page/post_add.html',context)

def delPost(request,num):
	post= Post.objects.get(id=num)
	post.delete()
	return HttpResponseRedirect('/admin_page/home/posts')

def catAll(request):
	all_cat=Category.objects.all()
	context = {'all_cat':all_cat}
	return render(request,'admin_page/category.html',context)

def catEdit(request,num):
	cat_obj=Category.objects.get(id=num)
	if(request.method=="POST"):
		cat_form=CategoryForm(request.POST,instance=cat_obj)
		if cat_form.is_valid():
			cat_form.save()
		return HttpResponseRedirect	("/admin_page/home/catAll")
	else:
		cat_form=CategoryForm(instance=cat_obj)
		context={'cat_form':cat_form}
		return render(request,'admin_page/cat_add.html',context)

def catDel(request,num):
	cat_obj=Category.objects.get(id=num)
	cat_obj.delete()
	return HttpResponseRedirect("/admin_page/home/catAll")


def catAdd(request):
	if request.method=="POST":
		cat_form=CategoryForm(request.POST)
		if cat_form.is_valid():
			cat_form.save()
		return HttpResponseRedirect("/admin_page/home/catAll")	
	else:
		cat_form=CategoryForm()
		context={
			'cat_form':cat_form,
			'title':'Add'
			}
		return render(request,"admin_page/cat_add.html",context)

# def userSearch(request,username):


