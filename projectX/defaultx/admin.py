from django.contrib import admin

# Register your models here.
from .models import UploadCategories, UploadProduct, UploadProduct_02

admin.site.register(UploadCategories)
admin.site.register(UploadProduct)
admin.site.register(UploadProduct_02)