from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'resume'
urlpatterns = [
    path('', home, name = 'home')
]
