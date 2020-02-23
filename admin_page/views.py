from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse,HttpResponseRedirect
from admin_page.forms import UserForm
# Create your views here.
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
		return HttpResponseRedirect("/admin_page/all")
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
		return HttpResponseRedirect("/admin_page/all")
	else:
		user_form=UserForm(instance=user)
		context={'user_form':user_form}
		return render(request,'admin_page/st_add.html',context)

def deleteUser(request,num):
	user = User.objects.get(id = num)
	user.delete()
	return HttpResponseRedirect('/admin_page/all')
