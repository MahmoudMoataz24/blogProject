from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.form import RegisterForm, LoginForm


@login_required
def index(request):
    return HttpResponse("<h1>Home</h1>")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account for {username}')
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegisterForm})
