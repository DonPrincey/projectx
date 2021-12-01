from django.forms import ModelForm
from django import forms
from .models import *
class UploadProductForm(forms.ModelForm):
      
      class Meta:
          #model=UploadProduct
          model = UploadProduct_02
          fields="__all__"

class UploadCategoryForm(forms.ModelForm):
      
      class Meta:
          model=UploadCategories
          fields="__all__"
          
class SearchBarForm(forms.Form):
    CHOICES=(("SHIRTS","SHIRTS"),
    ("JEANS","JEANS"),
    ("WOMENS","WOMENS"))
    searchqueryentry=forms.CharField(label="Type in item to search") 
    searchquery=forms.CharField(label="Categories",widget=forms.Select(choices=CHOICES))