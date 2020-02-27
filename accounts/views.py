from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.form import RegisterForm
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import userState


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = [form.cleaned_data.get('email')]
            send_mail("Welcome to OS BLOG", f"Thnak you {username} for your registration",
                      settings.EMAIL_HOST_USER, email, fail_silently=True)
            messages.success(request, f'Successfully created account for {username}')
            user = User.objects.last()
            userState.objects.create(user=user)
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': RegisterForm})


def blockUser(request, ID):
    user = User.objects.get(id=ID)
    if not user.is_staff:
        user_state = userState.objects.get(user=user)
        user_state.is_blocked = not user_state.is_blocked
        user_state.save()
        print(user_state.is_blocked)
    return redirect('adminhome')

