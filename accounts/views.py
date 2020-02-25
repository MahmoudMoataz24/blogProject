from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.form import RegisterForm, LoginForm
from django.core.mail import send_mail
from django.conf import settings


@login_required
def index(request):
    return HttpResponse("<h1>Home</h1>")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = [form.cleaned_data.get('email')]
            send_mail("Welcome to OS BLOG", f"Thnak you {username} for your registration",
                      settings.EMAIL_HOST_USER,email, fail_silently=True)
            messages.success(request, f'Successfully created account for {username}')
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegisterForm})
