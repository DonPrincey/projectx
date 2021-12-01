from django import forms
from django.forms import ModelForm, fields
from .models import *
# from django.forms import ModelForm

class Messageform(forms.Form):
    names=forms.CharField(label="enter your names")
    email=forms.EmailField(label="enter user email")
    phone=forms.IntegerField(label="enter phone number")
    message=forms.CharField(label="enter message")

class Messageform(forms.ModelForm):
    class Meta:
        model= Message
        fields="__all__"

class user_form(forms.Form):
    names=forms.CharField(label="enter your names")
    email=forms.EmailField(label="enter user email")
    phone=forms.IntegerField(label="enter phone number")
    message=forms.CharField(label="enter message")

class UserForm(forms.Form):
    name=forms.CharField(label="Enter your names ")
    email=forms.CharField(label="Enter Email Address ")
    comment=forms.CharField(label="Enter your commmnt ")

class msgForm(forms.Form):
    fromemail=forms.CharField(label="Enter from email ")
    toemail=forms.CharField(label="Enter destination email ")
    message=forms.CharField(label="Type in your message ")

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model= Userfeedback
        fields="__all__"


class category(forms.ModelForm):
    class Meta:
        model=category
        fields="__all__"

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model=CreateCategory
        fields="__all__"
 
 
class UploadProductForm(forms.ModelForm):
    class Meta:
        model=UploadProduct
        fields="__all__"