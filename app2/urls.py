from django.urls import path
from app2.views import *
app_name='Nothing'
urlpatterns=[
    path('htmlpage/',htmlpage,name='htmlpage'),
]