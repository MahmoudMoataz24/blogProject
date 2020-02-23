from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url

from register.form import RegisterForm


def index(request):
    return render(request, 'register/Index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../login/')
        else:
            return HttpResponse('<h1>Invalid</h1>')
    else:
        return render(request, 'register/RegisterForm.html', {'form': RegisterForm})
