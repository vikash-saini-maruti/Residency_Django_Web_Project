
from django.shortcuts import render

from booking.models import Booking

def userform(request):
    
    return render(request,"booking/userform.html")

def booking(request):
    if request.method == "POST":
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            check_in=request.POST.get('check_in')
            room_type=request.POST.get('room_type')
            Booking.objects.create(name=name,email=email,check_in=check_in,room_type=room_type)
            
        except:
            
            pass
        
    return render(request,"booking/userform.html")


        


