from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse(' is a  boy')

def h1(request):
    return render(request,'h1.html')

def h2(request):
    return render(request,'h2.html')


