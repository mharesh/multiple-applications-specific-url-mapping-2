app_name='string'
from django.urls import path
from app1.views import *

urlpatterns=[
    path('first/',first,name='first'),
    path('h1/',h1,name='h1'),
    path('h2/',h2,name='h2'),
]