from unicodedata import name
from django.contrib import admin
from django.urls import path
from homie import views

urlpatterns = [
    path("",views.index,name="homie"),
    path("login",views.login,name="login"),
    path("contact.html",views.contact,name="contact"),
    path("register",views.registerr,name="register"),
    path("logout",views.logout,name='logout')
    ]