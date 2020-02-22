from django.shortcuts import render
<<<<<<< HEAD
# from django.views import generic
# from blog.models import Comments,Likes,Post,userAdds,reply,Category
# from admin_page.forms  import PostForm

# # Create your views here.
# def users(request):
#     queryset=userAdds.objects.all()
#     context ={'all_users' : queryset}
# 	return render(request, 'admin_page/users.html',context)

# def addPost(request):
#     form=PostForm()
#     if request.method=="POST":
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('posts/')
# 	else:	
# 		context = {'form':form}
# 		return render(request,'admin/add_post.html',context)

# def viewPost(reuqest):
#     po=Post.objects.get(Postid=num)
#     context={'Post':po}
#     return render(request,'admin_page/post_details.html',context)
=======
from django.views import generic
from blog.models import Comments,Likes,Post,userAdds,reply,Category
from admin_page.forms  import PostForm

# Create your views here.
def users(request):
    queryset=userAdds.objects.all()
    context ={'all_users' : queryset}
	return render(request, 'admin_page/users.html',context)

def addPost(request):
    form=PostForm()
    if request.method=="POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('posts/')
	else:	
		context = {'form':form}
		return render(request,'admin/add_post.html',context)

def viewPost(reuqest):
    po=Post.objects.get(Postid=num)
    context={'Post':po}
    return render(request,'admin_page/post_details.html',context)
>>>>>>> ac06e2f14be7d1aab3ac3196709d2ac6f07d85c7
