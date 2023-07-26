from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def new(request):
    return render(request,'new.html')

def new1(request):
    return render(request,'new1.html')

def alone(request):
    return HttpResponse('<h1>single alone in our life</h1>')