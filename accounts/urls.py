from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("register",views.registerr,name="register")
    
    
]