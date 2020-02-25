from django.contrib import admin
from admin_page import views
from django.urls import path,include

urlpatterns = [
	path('home/',views.catshow),
	path('home/posts',views.viewPost),
	path('home/all',views.viewAll),
	path('home/delst/<num>',views.deleteUser),
	path('home/editst/<num>',views.EditUser),
	path('home/addst',views.addUser),
	path('home/postadd',views.addPost),
	path('home/postdel/<num>',views.delPost),
	path('home/postedit/<num>',views.EditPost),
	path('home/catAll',views.catAll),
	path('home/catAdd',views.catAdd),
	path('home/catEdit/<num>',views.catEdit),
	path('home/catDel/<num>',views.catDel),
]
