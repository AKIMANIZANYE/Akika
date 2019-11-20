from django.shortcuts import render,redirect
from django.conf import settings


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def apply(request):
    return render(request, 'apply.html')

def student(request):
    return render(request, 'studentForm.html')

def business(request):
    return render(request, 'businessForm.html')

