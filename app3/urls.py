from django.urls import path
from app3.views import*
app_name='solo'
urlpatterns = [
    path('page/',page,name="page"),
    path('page1/',page1,name='page1'),
    path('single/',single,name='single'),
 
]