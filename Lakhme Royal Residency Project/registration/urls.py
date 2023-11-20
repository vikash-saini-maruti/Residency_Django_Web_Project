from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('regi/',views.regifx),
path('insertdata/',views.insertdata,name="insertdata")
]