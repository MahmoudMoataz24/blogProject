from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from register.form import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Registered</h1>')
        else:
            return HttpResponse('<h1>Invalid</h1>')
    else:
        return render(request, 'register/RegisterForm.html', {'form': RegisterForm})
