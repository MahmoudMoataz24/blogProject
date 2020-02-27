from django.contrib import admin
from admin import views
from django.urls import path,include

urlpatterns = [
	path('Intro/',views.Intro),
	path('home/', views.PostList, name='home'),
	path('home/posts',views.viewPost),
	path('home/all',views.viewAll, name="adminhome"),
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
	path('home/forAdd',views.forAdd),
	path('home/forAll',views.forAll),
	path('home/fordel/<num>',views.deleteFor),
	path('home/<post_id>/', views.post_details, name='post_detail'),
	path('home/catshow/<catID>',views.showcatPosts),
]
