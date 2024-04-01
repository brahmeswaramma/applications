from django.urls import path
from app3.views import *
app_name="anything"
urlpatterns=[
    path('SpurlMap/',SpurlMap,name='SpurlMap'),
]