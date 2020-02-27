from posts import views
from django.urls import path
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<postID>[\w])/$', views.showSinglePost),
    # url(r'^(?P<catID>[\w])/$', views.categories),
    path('cats/', views.categories, name='categories'),
    url(r'^cats/(?P<catID>[\w])/$', views.showcatPosts),
    # url(r'^(?P<postID>[\w])/(?P<postTitle>[\w]+)/$', views.liked),
    # url(r'^(?P<postID>[\w])/(?P<postTitle>[\w]+)/d/$', views.disliked),
]

#   url(r'^cats/(?P<catID>[\w])/(?P<postID>[\w])/$', views.liked),
#      url(r'^cats/(?P<catID>[\w])/(?P<postID>[\w])d/$', views.disliked),