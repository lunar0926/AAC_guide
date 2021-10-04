from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def resources(request):
    return render(request, 'resources.html')


def community(request):
    return render(request, 'community.html')


def contact(request):
    return render(request, 'contact.html')