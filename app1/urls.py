from django.urls import path
from app1.views import *
app_name="something"
urlpatterns=[
    path('string_response/',string_response,name='string_response'),
]