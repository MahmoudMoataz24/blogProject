from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse,HttpResponseRedirect
from admin_page.forms import UserForm,PostForm,CategoryForm

def viewAll(request):
	user=User.objects.all()
	print(user)
	context ={'all' : user}
	return render(request,'admin_page/home.html',context)

def addUser(request):
	if request.method == "POST":
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect("/admin_page/home/all")
	else:
		user_form =UserForm() 
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

# def userSearch(request,name):
# 	user=User.objects.filter(username__contains=name)
# 	context = {'user_form':user_form}
# 	return render(request,'admin_page/st')

def viewPost(request):
	all_posts = Post.objects.all()
	print(all_posts)
	context = {'all_posts':all_posts}
	return render(request,'admin_page/posts.html',context)

def viewPo(request):
	all_posts = Post.objects.all()
	print(all_posts)
	context = {'all_posts':all_posts}
	return render(request,'admin_page/admin_home.html',context)

def addPost(request):
	if request.method == "POST":
		post_form = PostForm(request.POST)
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

def catshow(request):
	all_cat=Category.objects.all()
	context = {'all_cat':all_cat}
	return render(request,'admin_page/admin_home.html',context)	

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


