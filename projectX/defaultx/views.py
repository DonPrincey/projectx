from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here. 
def makeCart(request):
       print("no cart....settingup cart")
       request.session['cart']={}
       request.session['cart']['entries']={}
       request.session['cart']['total']=0
       request.session['cart']['items']=0
       print(request.session['cart'])
       return (request.session['cart'])
def ShowCart(request):
       print("fetchin cart ...........")
       print(request.session['cart'])
    
    
def HomePage(request):
    crtsum=0
    crtqty=0
    dvl=[]
    dl=[]
    
    #del request.session['cart']
    if 'cart' in request.session:
       #pass
       ShowCart(request)
       #print("fetching live cart ...........")
       #print(request.session['cart'])
       
    if 'cart' not in request.session:
       #pass
       makeCart(request)
    AddItemTOCart_GetQty(request)
    AddItemTOCart_GetTotal(request)
    #carttotal = request.session['cart']['total'] 
    x=GetCart(request)
    carttotal=x[3]
    cartqty  = request.session['cart']['items']           
          
    from .models import UploadProduct_02,UploadCategories
    dtx =UploadProduct_02.objects.all()
    ctx =UploadCategories.objects.all()
    dtxcount =UploadProduct_02.objects.all().count()
    print("**********counting items ----", dtxcount)
    
    cc =UploadProduct_02.objects.values('productcategory')
    print('PRINTING ALL items in DB ******')
    cartx=[]
    for t in cc:
         u=t['productcategory']
         print(u)
         v = UploadCategories.objects.get(id=u)
         print(v.name)
         cartx.append(v.name)        
    cartitems =request.session['cart']['entries']  
    print(cartx) 
    data={'dtx':dtx,"count":dtxcount,"category":ctx,"search_category":cartx,
    "cartqty":cartqty,"cart_total":carttotal,"cartitems":cartitems}
    return render(request,"index.html",data)
    
    
    
    
    
# To make this point only available to logged in users, you need to use a login decorator
@login_required()
def AdminDashboard(request):
    return render(request,"admin_dashboard.html")
     
def UploadProduct(request):
    forms=UploadProductForm(request.POST or None)
     
    if request.method=="POST":
        forms=UploadProductForm(request.POST,request.FILES)
        if forms.is_valid():
           forms.save()
           return redirect("/default/viewallproducts")
    data={'forms':forms,'title':"Upload"}
    
    return render(request,"upload.html",data)
     
def CreateProductCategory(request):
    form=UploadCategoryForm(request.POST or None)
    if request.method=="POST":
        form=UploadCategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            form.save()
            return redirect("/default/viewcategories")
     
    data={'forms':form,'title':""}    
    return render(request,"default/CreateproductCategory.html",data)
    
    
def ViewallCategory(request):
     from .models import UploadCategories
     dtx =UploadCategories.objects.all()
     data={'dtx':dtx}
    
     return render(request,"default/ViewallCategory.html",data)   
def ViewallCategoryItems(request,cartegoryid):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.filter(productcategory=cartegoryid)     
     dtxcount =UploadProduct_02.objects.filter(productcategory=cartegoryid).count()
     print("Available items ",dtxcount)     
     data={'dtx':dtx,"dtxcount":dtxcount}    
     return render(request,"viewallcategoryitems.html",data)
     
def SearchCategoryItems(request,search1,search2):
     print("searching for .....",search1,search2)
     from .models import UploadProduct_02
     from .models import UploadCategories
     u= UploadProduct_02.objects.all()
     usearch=[]
     for i in u: 
         print(i.id ,"----",i.productcategory)
         if str(i.productcategory)==str(search1):
             print("GOT MATCH",search1)
             u= UploadProduct_02.objects.get(id=i.id)
             print(u)
             usearch.append(u)
         if str(i.productcategory)==str(search2):
             print("GOT MATCH",search2)
             u= UploadProduct_02.objects.get(id=i.id)
             print(u)
             usearch.append(u)
     print(usearch)
     
         
          
     data={"search":usearch}
     return render(request,"showsearchitems.html",data)
     
def SearchCategoryItemsBKUP(request,search1,search2):
     print("searching for .....",search1,search2)
     from .models import UploadProduct_02,UploadCategories
     xxx= UploadProduct_02.objects.all()
     cc =UploadProduct_02.objects.values('productcategory')
     print('PRINTING ALL items in DB ******')
     cartx=[]
     for t in cc:
         u=t['productcategory']
         print(u)
         v = UploadCategories.objects.get(id=u)
         print(v.name)
         cartx.append(v.name)         
     
     print(cartx)
     s1 =UploadCategories.objects.filter(name=search1)
     s2 =UploadCategories.objects.filter(name=search2)   
     
     s1count =UploadCategories.objects.filter(name=search1).count()
     if s1count:
         srch1 =UploadCategories.objects.get(name=search1)
         s1_ID=srch1.id
         print(type(s1_ID) )
         print("---------",s1count , s1_ID)
         print("  ******************same  ",srch1)
         srch1 =UploadProduct_02.objects.filter(productcategory=s1_ID)
         #srch1x =UploadProduct_02.objects.get(productcategory=s1_ID)
         print("  ******************same  ",srch1)
         #z =srch1.get()
         print( )
         print(type(srch1))
         for y in srch1:
             print(y)
     else:
         srch1={}
         
         
         
     s2count =UploadCategories.objects.filter(name=search2).count()
     if s2count:
         srch2 =UploadCategories.objects.get(name=search2)
         s2_ID=srch2.id
         print("---------",s2count , s2_ID)
         #srch2 =UploadProduct_02.objects.get(productcategory=s2_ID)
     else:
         srch2={}
     print("  ******************",srch1)
     #search1_count =UploadProduct_02.objects.filter(productcategory=search1).count()
     #search2_count =UploadProduct_02.objects.filter(productcategory=search2).count()
     from .models import UploadCategories
     dtx =UploadCategories.objects.all()
     for i in dtx:
         print(i.name)
     print("Available items ",s1count,s2count)
     data={'search1':srch1,'search2':srch2,'search1_count':s1count,'search2_count':s2count,"searchitem1":search1,"searchitem2":search2}
    
     return render(request,"showsearchitems.html",data)
     
def ViewallProducts(request):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.all()
     data={'dtx':dtx}
    
     return render(request,"viewall.html",data)
     
def UpdateProducts(request, id):
    obj=get_object_or_404(UploadProductModel, id=id)
    form=UploadProductForm(request.POST or None, instance=obj)
    context={'form':form}
    
    return render(request,'posts/updateproducts.html,context')
    
def EditorDeleteProducts(request):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.all()
     data={'dtx':dtx}
    
     return render(request,"default/editordelete.html",data)
     
def EditProducts(request,productid):
     from .models import UploadProduct_02
     dtx =get_object_or_404(UploadProduct_02,id=productid)
     form=UploadProductForm(instance=dtx or None)
     if request.method=="POST":
         form=UploadProductForm(request.POST,request.FILES,instance=dtx or None)
         if form.is_valid():
             obj=form.save(commit=False)
             obj.save()
             return redirect("/default/viewallproducts")
     context={'form':form}
     return render(request,"default/edit_or_delete.html",context)
     
def DeleteProduct(request, productid):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.get(id=productid)
     data={'dtx':dtx}
    
     return render(request,"default/deleteproduct.html",data)

def ConfirmDeleteProduct(request, productid):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.get(id=productid)
     data={'dtx':dtx}
     dtx.delete()
    
     return redirect("/default/viewallproducts")

def DeleteCartegory(request, productid):
     from .models import UploadCategories
     dtx =UploadCategories.objects.get(id=productid)
     data={'dtx':dtx}    
     return render(request,"default/deleteCategory.html",data)

def ConfirmDeleteCateory(request, productid):
     from .models import UploadCategories
     dtx =UploadCategories.objects.get(id=productid)
     dtx.delete() 
     return redirect("/default/viewcategories")

def AddItemTOCartSession_GetItemName(request, productid):
          from .models import UploadProduct_02
          dtx =UploadProduct_02.objects.get(id=productid)          
          name=dtx.productname
          return (name)
def AddItemTOCart_GetQty(request):
          total_qty=0
          j=request.session['cart']['entries']
          for k,v in enumerate(j):
             #print('..........getting entry items  qty')
             #print(k,v)
             #print('..........entry items  details')
             #print(j[v])
             #print('..........unit qty',j[v]['qty'])
             total_qty+=j[v]['qty']
             print('..........total cart  qty',j[v]['qty'])
          return (total_qty)
def AddItemTOCart_GetTotal(request):
          total=0
          j=request.session['cart']['entries']
          for k,v in enumerate(j):
             #print('..........getting entry items  qty')
             #print(k,v)
             #
             #print('..........entry items  details')
             #print(j[v])
             #print('..........unit qty',j[v]['qty'])
             #print('..........unit price',j[v]['qty'])
             unit_ttl=j[v]['qty']*j[v]['price']
             #print('..........unit total',unit_ttl)
             total+=unit_ttl
             print('..........cart total',total)
          return (total)          
def AddItemTOCartSession_Update(request,n):
             
              old_data=request.session['cart']['entries']
              g=request.session['cart']['entries'][n]
              #print("****Current...",g)
              #print("****Current qty...",g['qty'])
              #print("****Current total...",g['total'])
              newqty=g['qty']+1
              newtotal=newqty*g['price']              
              g['total']=newtotal
              g['qty']=newqty
              #print("****Updated qty...",newqty,g['qty'])
              #print("****Updated total...",newtotal,g['total'])
              #data={"name":g['name'],"price":g['price'],"image":g['image'],"pid":g['pid'],"qty":newqty,'total':newtotal}
              #print(n,"......deleting old data")
              #del request.session['cart']['entries'][n]
              #print(n,"......listing current cart")              
              #print(request.session['cart']['entries'])
              #print(n,"......updating current cart")
             #request.session['cart']['entries'][n]=data
              #request.session.save()
              print(old_data)
              #request.session['cart']['entries'][n]
              #return (newqty,newtotal)
              return ("")
def CartItem_Update(request,name,quantity,total):
              
              old_data=request.session['cart']['entries']
              g=request.session['cart']['entries'][name]
                           
              g['total']=int(total)
              g['qty']=int(quantity)              
              request.session.save()
              
              x=AddItemTOCart_GetTotal(request)              
              #rsi=name+"--"+str(x)
              rsi=x
              return HttpResponse(rsi)
          
              

              
def RemoveItemFromCartSession(request,itemname):
              n=itemname
              old_data=request.session['cart']['entries']
              g=request.session['cart']['entries'][n]
              oldttl=request.session['cart']['total']           
              oldqty=request.session['cart']['items']
              newqty=oldqty-g['qty']
              newtotal=oldttl-g['total']              
              request.session['cart']['total'] = newtotal
              request.session['cart']['items'] = newqty
              del request.session['cart']['entries'][n]
              request.session.save()
              new_data=request.session['cart']['entries']
              print("****After removing item data is :",new_data)
              
              return ("")          
def AddItem_CheckforitemInCartsession(request,cartsession,nameofitem):
         cartsession='cart'
         n=nameofitem
         ct=request.session['cart']
         if n not in ct.keys():
             print(n," not in CartSession")
             return (False,n,ct)
         if n in ct.keys():
             print(n," YES in CartSession")
             return (True,n,ct)
          
def AddItemToCartEntry(request, productid):
          dtx =UploadProduct_02.objects.get(id=productid)
          price=dtx.productprice
          name=dtx.productname
          image=str(dtx.productimage)
          pid=dtx.id
          qty=1
          total=price*qty
          data={"name":name,"price":price,"image":image,"pid":pid,"qty":qty,'total':total}         
          return(name,data,qty,total)
                    
          
def AddItemCart(request, productid):
        
        old_data=request.session['cart']['entries']
        itemname=AddItemTOCartSession_GetItemName(request, productid)
        #print(type(old_data))
        if itemname in old_data:
           print("item name is : ",itemname)
           print(" ******Updating this entry ..........")
           s=AddItemTOCartSession_Update(request,itemname)         
          
           request.session['cart']['total']=AddItemTOCart_GetTotal(request)           
           request.session['cart']['items']=AddItemTOCart_GetQty(request)
           request.session.save()
        if itemname not in old_data:
           d=AddItemToCartEntry(request, productid)           
           request.session['cart']['entries'][d[0]]=d[1]
           request.session['cart']['total']=AddItemTOCart_GetTotal(request)           
           request.session['cart']['items']=AddItemTOCart_GetQty(request)           
           request.session.save() 
        print("showing updated data.....")
        ShowCart(request)
        return redirect("/")
    
def RemoveThisItemFromCart(request,itemname):
        
        old_data=request.session['cart']['entries']
        #itemname=AddItemTOCartSession_GetItemName(request, productid)
        #print(type(old_data))
        if itemname in old_data:
           print("item name is : ",itemname)
           print(" ******Removing this entry ..........")
           #s=AddItemTOCartSession_Update(request,itemname)         
           rem = RemoveItemFromCartSession(request,itemname)  
           request.session['cart']['total']=AddItemTOCart_GetTotal(request)           
           request.session['cart']['items']=AddItemTOCart_GetQty(request)
           request.session.save()
        if itemname not in old_data:
           messages.success(request,"This item is not in your cart !")
           return redirect("/default/viewitemsincart")
        print("showing updated data.....")
        ShowCart(request)
        messages.success(request,"The item was removed from your cart !")
           
        return redirect("/default/viewitemsincart") 
def DeleteCartSession(request):
      if 'cart'  in request.session:
         del request.session['cart']         
      if 'cartitemnames'  in request.session:
         del request.session['cartitemnames']
      return redirect("/default/admindashboard")
     
def DeleteCartItems(request, productid):
     from .models import UploadProduct_02
     dtx =UploadProduct_02.objects.get(id=productid)
     data={'dtx':dtx}
    
     return render(request,"default/deleteproduct.html",data)

def GetCart(request):
    ttlx=0
    qtyx=0
    if 'cart' in request.session:
        x=carttotal = request.session['cart']['total']           
        y=cartqty  = request.session['cart']['items'] 
        z=request.session['cart']['entries']
        for x in z:
            print("***>>",x,z[x]['name'])
            print("-----::",z[x]['qty'],z[x]['total'])
            qtyx+=z[x]['qty']
            ttlx+=z[x]['total']
            
    if 'cart' not in request.session:
         x=0
         y=0
         z=0
    print("GetCart Data:",ttlx,qtyx)
    return (x,y,z,ttlx,qtyx)

def ViewItemsInCart(request):
     ax=GetCart(request)
     data={"pagetitle":"View Shop Cart Items ","cartitems":ax[2]
     ,"total":ax[0],"qty":ax[1]}    
     return render(request,"default/view_itemsincart.html",data)

def RemoveItemsFromCart(request):
     ax=GetCart(request)
     
     data={"pagetitle":"Remove items from your Cart",
     "cartitems":ax[2],"total":ax[0],"qty":ax[1]}    
     return render(request,"default/view_itemsincart.html",data)
 

def CartCheckOut(request):
     ax=GetCart(request)
     #the above returns     return (x,y,z,ttlx,qtyx)
     #the ttlx and qtyx ,i use to get updated values
     data={"pagetitle":"Check out here","cartitems":ax[2]
     ,"total":ax[0],"qty":ax[1],"updated_total":ax[3],
     "updated_qty":ax[4],}
     y=AddItemTOCart_GetQty(request)
     z=AddItemTOCart_GetTotal(request)     
     print("-------",ax)
     print("-------",ax[0],ax[1])  
     print("------->>",y,z,ax[3],ax[4])
     return render(request,"default/cart_checkout.html",data)
def MakePayment(request,totalamount):
       
     return redirect("http://www.paystack.com")
 
def TestJsonData(request):
    import requests
    from django.http import JsonResponse
    from django.core import serializers
    url="https://api.coincap.io/v2/assets/bitcoin"
    
    response = requests.get(url)
    jsp = dict(response.json())
     
    return render (request,"test_json.html")
    #return HttpResponse(url)
 
def TestJsonDataBkup(request):
    import requests
    from django.http import JsonResponse
    from django.core import serializers
    url="https://api.coincap.io/v2/assets/bitcoin"
    #return HttpResponse(json.dumps(url), content_type='application/json')
    response = requests.get(url)
    jsp = response.json()
    djsp=dict(jsp)
    print("Printing the dict data : ",jsp)
    y=serializers.deserialize('json',jsp)
    print ("...........",type(y))
    print ("...........",type(jsp))
    print ("...........",type(djsp))
    for key in djsp:
       print ("printing key : ",key)
       print ("printing data : ",djsp[key])
       print(type(djsp[key]) )
       if key == 'data':
          a=djsp[key]
          for key in a:
            print(key," -:-",a[key])
    return HttpResponse(url)