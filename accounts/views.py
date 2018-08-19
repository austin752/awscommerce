from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm(request.POST or None)
    content = {
        'form': form
    }
    next_ = request.GET.get('next')
    next_page = request.POST.get('next')
    redirect_path = next_ or next_page or None
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(redirect_path)
            if is_safe_url(redirect_path, request.get_host()):
	            #return redirect(redirect_path)
                print(next_)
                return redirect(redirect_path)
        else:
            return redirect('/')
    return render(request, 'accounts/login.html', content)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    content = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('accounts/register.html')
    return render(request, 'accounts/register.html', content)

