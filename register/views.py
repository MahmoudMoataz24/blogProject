from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from register.form import RegisterForm


def index(request):
    return render(request, 'register/Index.html')


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
        return render(request, 'register/RegisterForm.html', {'form': RegisterForm})
    return render(request, 'register/RegisterForm.html', {'form': form})
