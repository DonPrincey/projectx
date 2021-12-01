from django.shortcuts import render
from projectX.forms import *
from .models import *


# Create your views here.
def HomePage(request):   
    data={}
    return render(request, "index.html",data)
def PostItem(request):   
    data={}
    return render(request, "index.html",data)
def ViewAll(request):   
    data={}
    return render(request, "index.html",data)
def ViewDetails(request):   
    data={}
    return render(request, "index.html",data)
def AddToCart(request):   
    data={}
    return render(request, "index.html",data)

def UploadProduct(request):   
    data={}
    return render(request, "index.html",data)
    
