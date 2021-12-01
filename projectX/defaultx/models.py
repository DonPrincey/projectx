from django.db import models

# Create your models here.




class UploadCategories(models.Model):
    name=models.CharField("Category Name",max_length=100)
    feature=models.CharField("Feature Category",max_length=100)
    description=models.CharField("ProductDescription",max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'UploadCategories'
        
class UploadProduct(models.Model):
    productname=models.CharField("ProductName",max_length=100)
    #productcategory=models.ForeignKey("UploadCategories",on_delete=models.CASCADE)
    category=models.CharField("Default Category",max_length=100)
    productprice=models.IntegerField("ProductPrice")
    description=models.CharField("ProductDescription",max_length=200)
    productimage=models.ImageField("ProductImage",upload_to="productuploads")
    def __str__(self):
        return self.productname+" -- "+self.description+" -- "+self.category

    class Meta:
        verbose_name_plural = 'UploadProduct'


class UploadProduct_02(models.Model):
    productname=models.CharField("ProductName",max_length=100)
    productcategory=models.ForeignKey("UploadCategories",on_delete=models.CASCADE)    
    productprice=models.IntegerField("ProductPrice")
    description=models.CharField("ProductDescription",max_length=200)
    productimage=models.ImageField("ProductImage",upload_to="productuploads")
    def __str__(self):
        return self.productname+" -- "+str(self.productprice)

    class Meta:
        verbose_name_plural = 'UploadProduct_02'
