app_name='bad time'
from django.urls import path
from app2.views import *

urlpatterns=[
    path('new/',new,name='new'),
    path('new1/',new1,name='new1'),
    path('alone/',alone,name='alone'),
]