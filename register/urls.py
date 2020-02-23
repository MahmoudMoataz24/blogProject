from django.urls import path
from register import views as register_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='register/LoginFrom.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/LogOUT.html'), name='logout'),

]
