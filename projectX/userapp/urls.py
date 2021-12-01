from django.contrib import admin
from django.urls import path, include
from .views import *
# Create your tests here.
app_name="userapp"

urlpatterns=[

    path("cvfgtyhu",Userindex, name="index"),
    path("userform",uForm, name="userform"),
    path("usermessage",userMessage, name="usermessage"),
    path("userfeedback",userFeedback, name="userfeedback"),
    path("userfeedbacks",UserFeedbackView, name="userfeedbacks"),
    path("userlogout",UserLogout, name="userlogout"),
    path("sendmessage",SendMessage, name="sendmessage"),
    path("messageform",msgFormx, name="messageform"),
    path("payment",UserPayment, name="payment"),
    path("gotohomepage",UserRegister,name="gotohomepage"),
    
     path('',HomePage,name='homepage'),
   
    path('',include('django.contrib.auth.urls')),
    path('home',HomePage,name='home'),
    
    path('viewdetail/',ViewDetails,name="viewdetail"),
    path('addtocart/',AddToCart,name="addtocart"),
    path('uploadproducts/',UploadProduct,name="uploadproducts"),
    path('createcategory/',UploadCategory,name="createcategory"),
    path('viewcategory/',ViewCategory,name="viewcategory")
    
    
  
]
