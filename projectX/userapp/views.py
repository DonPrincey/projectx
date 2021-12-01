from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import *
from .models import *
# Create your views here.
def UserRegister(request):
    #return HttpResponse(request.method)
    myform=UserCreationForm(request.POST or None)
    if(request.method=="POST"):
        if myform.is_valid():
            user=myform.save()
            # login(request,user)
            # messages.success(request, "Success: You are logged in")
            return redirect("/userapp/login")
    data={"form":myform, "title":"User Registration"}
    return render(request,"registration/register.html", data)

def UserLogout(request):
    txt="You are logged out"
    data={"text":txt}
    return render(request, "registration/logout.html",data)

def userFeedback(request):
    if request.method=="POST":
        form= UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/userapp/userfeedbacks")
    form=UserFeedbackForm()
    data={"form":form}
    return render (request, "usermessage.html",data)

def UserFeedbackView (request):
    u=Userfeedback.objects.all()
    data={"u":u}
    return render(request, "feedback.html", data)

def SendMessage (request):
    u= Messageform()
    data={"forms":u}
    return render (request, "usermessage.html", data)

def userMessage (request):
    if request.method=="POST":
        u= user_form(request.POST)
        print(request.POST("names"))
        print(request.POST("email"))
        print(request.POST("phone"))
        print(request.POST("message"))
    u= user_form(initial={"names":"Emaks"})
    data={"forms":u}
    return render (request, "usermessage.html", data)

def uForm (request):
    dt="Please post your comment"
    bt="submit comment"
    df=UserForm()
    data={"df":df,"formtitle":dt,"buttontext":bt}
    return render(request, "blank_form.html",data)
    
def msgFormx (request):
    dt="Send your message"
    bt="send message"
    df=msgForm()
    data={"df":df,"formtitle":dt,"buttontext":bt}
    return render(request, "blank_form.html",data)
    
def Userindex (request):
    data={"dtitle":"user home page"}
    return render(request,"index.html",data)
    
def UserPayment (request):
    itm="Shirt"
    unt=5000
    qty=5
    ttl=unt*qty
    data={"items":itm,"unitprice":unt,"quantity":qty,"total":ttl}
    return render(request,"payment.html",data)
    
def HomePage(request):
    return HttpResponse("<h3>Welcome!</h3>")
    
def Custom(request, name):
    n= name
    print("Welcome mr ",n)
    return HttpResponse("<h3>Welcome!</h3>")
    
def Confirmation(request,name,item,cash,quantity):
    n= name
    i=item
    c=cash
    q=quantity
    t=c*q
    print("Your order mr ",n,"Items: ",i,"Unit Amount: ",c,"Quantity: ",q,"Total Amount: ",t)
    return HttpResponse("<h3>Your order mr "+n+"<br>items: "+i+"<br>Unit Amount"+str(c)+"<br>Quantity"+str(q)+"<br>Total amount:"+str(t)+"</h3>")
    
def Reserve(request,name,dst,dtype):
    print("Your order mr/mrs/** ",name,"distination: ",dst,"Triptype: ",dtype)
    return HttpResponse("<h3>Your reservation mr "+name+"<br>distination: "+dst+"<br>Trip type: "+dtype+"</h3>")

def HomePage(request):
    return render(request,"index.html")


def UploadCategory(request): 
    forms=CreateCategoryForm(request.POST or None)
    print("^^^^^^^^^^^^",request.method)
    if request.method=="POST":        
        if forms.is_valid():
           forms.save()
           return redirect("/viewallcategory")
    data={'forms':forms}
    return render(request,"blank_form.html",data)
    
def ViewCategory(request): 
    from .models import category
    x = category.object.all()
    data={'all':x}
    return render(request, "blank_form.html",data)
   
def UploadProduct(request): 
    form=UploadProductForm(request.POST or None)
    if request.method=="POST":
        form=UploadForm(request.POST,request.FILES)
        if forms.is_valid():
            fors.save()
            return redirect("instashop/viewallproducts")
    data={'forms':forms}
    return render(request, "blank_form.html",data)
    
def ViewDetails(request):
    return HttpResponse("<h3>Welcome!</h3>")
def AddToCart(request):
    return HttpResponse("<h3>What would you like to add!</h3>")
  