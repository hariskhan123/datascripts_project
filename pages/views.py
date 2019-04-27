from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'pages/index.html')

def blog(request):
  return render(request, 'pages/blog.html')

def pos(request):
  return render(request, 'pages/pos.html')