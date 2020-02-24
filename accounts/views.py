from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.form import RegisterForm, LoginForm


@login_required
def index(request):
    return render(request, 'accounts/Index.html', {})


def login(request):
    return render(request, 'accounts/login.html', {'form': LoginForm})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Successfully created account for {username}')
            return redirect('login')
    else:
        return render(request, 'accounts/register.html', {'form': RegisterForm})
    return render(request, 'accounts/register.html', {'form': form})
