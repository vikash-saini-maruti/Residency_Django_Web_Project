from django.urls import path
from . import views

urlpatterns = [
    path('userform/',views.userform),
    path('bookingform/',views.booking,name="booking")
]
