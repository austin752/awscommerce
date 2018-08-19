from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import ContactForm


def home_page(request):
    content = {
        'Title': 'Home page',
        'premium content': 'yehhh'
    }
    if request.user.is_authenticated():
        content = {
            'premium content': 'yeahhh'
        }
    return render(request, 'home.html', content)


def contact_page(request):
    form = ContactForm(request.POST or None)
    content = {
        'Title': 'Contact page',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'contact.html', content)


def about_page(request):
    content = {
        'Title': 'About page',
        'message':'this sucks!'
    }
    return render(request, 'about.html', content)
