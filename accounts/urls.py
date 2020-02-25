from django.conf.urls import url
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, \
    PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    path('register/', accounts_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('index/', accounts_views.index, name='index'),

    path('password_reset/', PasswordResetView.as_view(template_name='accounts/passreset.html'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='accounts/passresetdone.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/passresetcomplete.html'), name='password_reset_complete'),

]
