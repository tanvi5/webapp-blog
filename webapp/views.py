from django.shortcuts import render
from webapp import views
# from django.http import HttpResponse

def index(request):
    return render(request,'webapp/base.html')

def home(request):
    return render(request,'webapp/home.html')

def about(request):
    return render(request,'webapp/about.html')

def new_post(request):
    return render(request,'webapp/new_post.html')

def drafts(request):
    return render(request,'webapp/drafts.html')

# Create your views here.
