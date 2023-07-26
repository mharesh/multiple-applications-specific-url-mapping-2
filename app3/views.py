from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page(request):
    return render(request,'page.html')

def page1(request):
    return render(request,'page1.html')

def single(request):
    return HttpResponse('<h1>python full stack development</h1>')