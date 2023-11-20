from django.contrib import admin
from django.urls import path
from ourservice import views


urlpatterns = [
    
    path('ourservice/',views.ourservicefx ),
]