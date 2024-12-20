from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(req):
    return render(req,'add.html')

def add(req):
    if req.method=='POST':
        name=req.POST['c_name']
        data=Category.objects.create(c_name=name)
        data.save()
        return redirect(add)
    else:
        return render(req,'add.html')

def add_plants(req):
    #  if 'shop' in req.session:
          
        if req.method=='POST':
            id=req.POST['p_id']
            name=req.POST['name']
            type=req.POST['p_type']
            price=req.POST['price']
            img=req.FILES['img']
            stock=req.POST['stock']
            disp=req.POST['disp']
            data=plants.objects.create(p_id=id,name=name,p_type=type,price=price,img=img,stock=stock,disp=disp)
            data.save()
            return redirect(add)
            
        else:
            return render(req,'add_plants.html')