from django.db import models

# Create your models here.

class Message (models.Model):
    names=models.CharField("Enter your name",max_length=100)
    email=models.EmailField("Enter your name")
    phone=models.IntegerField("Enter your name",max_length=100,default=1234567)
    message=models.TextField("Enter your message")

class Userfeedback(models.Model):
    names=models.CharField("Enter your names", max_length=100)
    email=models.EmailField(("Enter your email"), max_length=100)
    phone=models.IntegerField(("Enter your phone number"))
    message=models.TextField(("Enter your feedback message"))
    def __str__(self):
        return self.names
class category(models.Model):
    name = models.CharField("Category name",max_length=100)
    description = models.CharField("Category description",max_length=100,default="null value")
    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField("Product Image",null=False, blank=False, upload_to='products')
    name = models.CharField("Product name",max_length=200,null=False, blank=False)
    price = models.IntegerField("Product Price",default=00000)
    category = models.ForeignKey(category,on_delete=models.CASCADE,default="null value") #if we delete this category the product will also be deleted 
    description = models.TextField("Product Description")
    
    def __str__(self):
        return self.name
        
        

class UploadProduct(models.Model):
    image = models.ImageField("Product Image",null=False, blank=False, upload_to='products')
    name = models.CharField("Product name",max_length=200,null=False, blank=False)
    price = models.IntegerField("Product Price",default=00000)
    description = models.TextField("Product Description",default="null value")
    
    def __str__(self):
        return self.name
        
class CreateCategory(models.Model):
      name = models.CharField("Category name",max_length=100)
      desc = models.CharField("Category description",max_length=100)
      def __str__(self):
        return self.name