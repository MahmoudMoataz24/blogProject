from django.contrib import admin
from admin_page import views
from django.urls import path,include

urlpatterns = [
	path('posts',views.Post),
	path('all',views.viewAll),
	path('delst/<num>',views.deleteUser),
	path('editst/<num>',views.EditUser),
	path('addst',views.addUser),
]
