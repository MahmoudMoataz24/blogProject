from django.contrib import admin
from admin_page import views
from django.urls import path,include

urlpatterns = [
	path('posts',views.viewPost),
	path('all',views.viewAll),
	path('delst/<num>',views.deleteUser),
	path('editst/<num>',views.EditUser),
	path('addst',views.addUser),
	path('postadd',views.addPost),
	path('postdel/<num>',views.delPost),
	path('postedit/<num>',views.EditPost),
	# path('catAll',views.catAll),
	# path('catAdd',views.catAdd),
	# path('catEdit/<num>',views.catEdit),
	# path('catDel/<num>',views.catDel),
]
