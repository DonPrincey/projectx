from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# Create your tests here.
app_name="default"

urlpatterns=[
path('',HomePage,name='home'),
path('default/uploadproduct',UploadProduct,name='uploadproduct'),
path('default/viewallproducts',ViewallProducts,name='viewallproducts'),
path('default/updateproduct',UpdateProducts,name='updateproducts'),
path('default/editordelete',EditorDeleteProducts,name='editorupdate'),
path('default/deleteproduct/<int:productid>',DeleteProduct,name='deleteproduct'),
path('default/confirmdeleteproduct/<int:productid>',ConfirmDeleteProduct,name='confirmdeleteproduct'),
path('default/editproduct/<int:productid>',EditProducts,name='editproducts'),
path('default/admindashboard',AdminDashboard,name='admindashboard'),
path('default/createproductcategory',CreateProductCategory,name='createcategory'),

path('default/viewcategories',ViewallCategory,name='viewcategory'),
path('default/viewcategoryitems/<int:cartegoryid>',ViewallCategoryItems,name='viewcategoryitems'),
path('default/searchitems/<str:search1>/<str:search2>',SearchCategoryItems,name='searchitems'),
path('default/deletecategory/<int:cartegoryid>',DeleteCartegory,name='deletecategory'),
path('default/confirmdeletecategory/<int:cartegoryid>',ConfirmDeleteCateory,name='confirmdeletecategory'),
path('default/additemtocart/<int:productid>',AddItemCart,name='additemstocart'),
path('default/viewitemsincart/',ViewItemsInCart,name='viewitemsincart'),
path('default/deletecartitems/',DeleteCartItems,name='deletecartitems'),
path('default/removeitemsfromcart/',RemoveItemsFromCart,name='removeitemsfromcart'),
path('default/removethisitemfromcart/<str:itemname>',RemoveThisItemFromCart,name='removethisitemfromcart'),
path('default/checkout/',CartCheckOut,name='checkout'),
path('default/cartItemupdate/<str:name>/<int:quantity>/<int:total>',CartItem_Update,name='cartitemupdate'),
path('default/makepayment/<int:totalamount>/',MakePayment,name='checkout'),
path('default/deletecartsessions/',DeleteCartSession,name='deletecartsessions'),
path('default/testjsonurldata/',TestJsonData,name='testjsonurldata'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
