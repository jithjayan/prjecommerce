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
        return ("dddd")
