import os
import uuid


from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from ecommerce_site.settings import EMAIL_HOST_USER


# Create your views here.

def index(request):
    return render(request,'index.html')

def navbar(request):
    return render(request,'navbar.html')

def shopregisterview(request):
    if request.method=='POST':
        a=shopform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            email=a.cleaned_data['email']
            phone=a.cleaned_data['phone']
            password=a.cleaned_data['password']
            cpassword=a.cleaned_data['cpassword']
            if password==cpassword:
                b=shopmodel(username=username,email=email,phone=phone,password=password)
                b.save()
                return redirect(shoplogin)
            else:
                return HttpResponse("registration Failed")
    return render(request,'register_shop.html')


def userregisterview(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            pasw=a.cleaned_data['password']
            cpasw=a.cleaned_data['cpassword']
            if pasw==cpasw:
                b=usermodel(username=us,email=em,phone=ph,password=pasw)
                b.save()
                return redirect(userlogin)
            else:
                return HttpResponse("registration Failed")
    return render(request,'register_user.html')


def shoplogin(request):
    if request.method=='POST':
        a=shoploginform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            b=shopmodel.objects.all()
            for i in b:
                # user=i.username
                # global
                # 1st method
                # request.session['user']=user  # b=request.session['user']
                # 2nd method
                # global val
                # def val():
                #     return user
                if username==i.username and password==i.password:
                    return render(request,'shop_profile.html',{'user':i.username,'email':i.email,'id':i.id})
            else:
                return HttpResponse("Login failed")
    return render(request,'shop_login.html')


def userlogin(request):
    if request.method=='POST':
        a=userloginform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            b=usermodel.objects.all()
            for i in b:
                request.session['user']=i.username
                request.session['email']= i.email
                if username==i.username and password==i.password:
                    return redirect(userprofileview)
            else:
                    return HttpResponse("Login failed")
    return render(request,'user_login.html')


def addproductview(request):
    if request.method=='POST':
        a=addproductform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['name']
            id=a.cleaned_data['proid']
            im=a.cleaned_data['image']
            pr=a.cleaned_data['price']
            ds=a.cleaned_data['description']
            b=addproductmodel(name=nm,proid=id,image=im,price=pr,description=ds)
            b.save()
            return redirect(viewproductview)
        else:
            return HttpResponse("adding failed")
    return render(request,'add_product.html')

def viewproductview(request):
    a=addproductmodel.objects.all()
    nm=[]
    proid=[]
    im=[]
    pr=[]
    ds=[]
    id=[]
    for i in a:
        nm.append(i.name)
        proid.append(i.proid)
        im.append(str(i.image).split('/')[-1])
        pr.append(i.price)
        ds.append(i.description)
        id.append(i.id)
        mylist=zip(nm,proid,im,pr,ds,id)
    return render(request,'view_product.html',{'mylist':mylist})

def productdeleteview(request,id):
    a=addproductmodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(viewproductview)

def editshopview(request,id):
    a=shopmodel.objects.get(id=id)
    if request.method=='POST':
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(shoplogin)

    return render(request,'edit_shop.html',{'a':a})


def editproductsview(request,id):
    a=addproductmodel.objects.get(id=id)
    im=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.name=request.POST.get('name')
        a.price=request.POST.get('price')
        a.description=request.POST.get('description')
        a.save()
        return redirect(viewproductview)
    return render(request,'edit_products.html',{'a':a,'im':im})

def userprofileview(request):
    a = addproductmodel.objects.all()
    b=request.session['user']
    nm = []
    proid = []
    im = []
    pr = []
    ds = []
    id = []
    for i in a:
        nm.append(i.name)
        proid.append(i.proid)
        im.append(str(i.image).split('/')[-1])
        pr.append(i.price)
        ds.append(i.description)
        id.append(i.id)
        mylist = zip(nm, proid, im, pr, ds, id)
    return render(request, 'user_profile.html', {'mylist': mylist,'b':b})

def viewcartview(request):
    a = cartmodel.objects.all()
    name = []
    image = []
    price = []
    des = []
    id = []
    pr=[]
    for i in a:
        pr.append(i.proid)
        id.append(i.id)
        price.append(i.price)
        des.append(i.description)
        name.append(i.name)
        im = str(i.image).split('/')[-1]
        image.append(im)
        mylist = zip(id, name, image, price, des,pr)
    return render(request, 'view_cart.html', {'mylist': mylist})


def addtocartview(request,id):
    a=addproductmodel.objects.get(id=id)
    b=cartmodel(name=a.name,proid=a.proid,image=a.image,description=a.description,price=a.price)
    b.save()
    return redirect(viewcartview)

def deletecart(request,id):
    a=cartmodel.objects.get(id=id)
    a.delete()
    return redirect(viewcartview)

# def buyfromcartview(request):
#     a=cartmodel.objects.all()
#     nm=[]
#     pr=[]
#     proid=[]
#     for i in a:
#         nm.append(i.name)
#         pr.append(i.price)
#         proid.append(i.proid)
#         mylist=zip(nm,pr,proid)
#     itn=[]
#     itp=[]
#     itq=[]
#     total=[]
#     amount = 0
#     for i in mylist:
#         if request.method=='POST':
#             itn.append(request.POST.get('name'))
#             itp.append(request.POST.get('price'))
#             itq.append(request.POST.get('quantity'))
#             total.append( int(request.POST.get('price')) * int(request.POST.get('quantity')))
#             bill=zip(itn,itp,itq,total)
#             for i in total:
#                amount=amount+i
#         return render(request,'bill.html',{'amount':amount})
#     return render(request,'buyfromcart.html',{'mylist':mylist})

def buy(request,id):
    a = cartmodel.objects.get(id=id)
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_price = request.POST.get('price')
        item_quantity = request.POST.get('quantity')
        total = int(item_price) * int(item_quantity)
        request.session['total']=total
        request.session['name']=item_name
        request.session['price']=item_price
        return render(request, 'billitem.html', {'itn': item_name, 'itp': item_price, 'itq': item_quantity, 't': total})
    return render(request, 'buy.html', {'a': a})

def email_send(request):
    a=contactusform()
    user=request.session['user']
    b=request.session['total']
    c=request.session['name']
    d=request.session['email']
    if request.method=='POST':
        sub=contactusform(request.POST)
        if sub.is_valid():
            nm=sub.cleaned_data['name']
            em=sub.cleaned_data['email']
            ms=sub.cleaned_data['message']
            send_mail(str(nm)+"||"+"Final bill",ms,EMAIL_HOST_USER,[em])
            return render(request,'success.html')
    return render(request,'email.html',{'form':a,'b':b,'c':c,'d':d,'user':user})


def success(request):
    return render(request,'success.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def logoutshop(request):
    return redirect(shoplogin)

def logoutuser(request):
    return redirect(userlogin)