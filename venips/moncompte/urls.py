from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
path('moncompte',moncompte,name="moncompte")
    
]
