from django.contrib import admin
from django.urls import path
from review import views

urlpatterns = [
    path('review/',views.reviewfx),
    path('inputreview/',views.inputreview),
    path('savereview/',views.savereview, name="savereview")
     
    
]