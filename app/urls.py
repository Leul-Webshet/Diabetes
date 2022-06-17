from unicodedata import name
from django import views
from django.urls import path
from .views import predict,info
urlpatterns=[
    path('',predict,name='test'),
    path('info',info,name='info')
    ]