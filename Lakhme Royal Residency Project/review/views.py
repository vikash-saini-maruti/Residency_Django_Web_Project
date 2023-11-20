from django.shortcuts import render
from review.models import Review


def reviewfx(request):
    reviewdatavar=Review.objects.all()
    reviewdata = {
        'reviewtable':reviewdatavar
        
    }
    return render(request, 'review/review.html',reviewdata)

def inputreview(request):
    return render(request,'review/inputreview.html')

def savereview(request):
    name = request.POST['name']
    star = request.POST['star']
    review = request.POST['review']
    suggestion = request.POST['suggestion']
    newuser = Review.objects.create(name=name,star=star,review=review,suggestion=suggestion)
    return render(request,"review/reviewdone.html")


    

# Create your views here.



