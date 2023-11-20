from django.shortcuts import render
from registration.models import regi

def regifx(request):
    return render(request,'registration/regi.html')

def insertdata(request):
    fname = request.POST['fname']  #THIS IS METHOD OF STORING DATA FROM HTML PAGE TO THESE VAR
    contact = request.POST['contact']
    aadhar = request.POST['aadhar']
    address = request.POST['address']

    newuser = regi.objects.create(name=fname,contact=contact,adhar=aadhar,address=address) #THIS IS STORING THESE VAR TO MODULE TABLE
    return render(request,"registration/successfullpage.html")









