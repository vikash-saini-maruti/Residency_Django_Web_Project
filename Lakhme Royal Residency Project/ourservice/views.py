from django.shortcuts import render
from ourservice.models import Ourservice


def ourservicefx(request):
    ourservicefatch= Ourservice.objects.all()
    servicedata = {
        'servicedic':ourservicefatch
    }
    return render(request,'ourservice.html',servicedata)
    

# Create your views here.
