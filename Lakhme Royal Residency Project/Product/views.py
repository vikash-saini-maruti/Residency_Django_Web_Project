from django.shortcuts import render
from Product.models import Product


def Productfx(request):
    Productfatch= Product.objects.all()
    Productdata = {
        'Productdic':Productfatch
    }
    return render(request,'product.html',Productdata)