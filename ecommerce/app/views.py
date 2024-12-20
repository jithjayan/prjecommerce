from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def m_login(req):
    if 'user' in req.session:
        return redirect(user_prfl)
    if req.method=='POST':
        uname=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(admin_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid uname or password")
            return redirect(m_login)
    else:
        return render(req,'login.html')


def reg(req):
        if req.method=='POST':
            name=req.POST['name']
            email=req.POST['email']
            password=req.POST['password']
            try:
                send_mail('user registration', 'account created', settings.EMAIL_HOST_USER, [email])
                data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
                data.save()
                return redirect(m_login)
            except:
                messages.warning(req,"Email not valid")
                return redirect(reg)
        else:
            return render(req,'user/register.html')

def admin_home(req):
    data=Category.objects.all()
    return render(req,'admin/adminhome.html',{'Category':data})

def user_home(req):

    data=Plants.objects.all()[::-1]
    return render(req,'user/userhome.html',{'Plants':data})
def homep(req):
    return redirect(user_home)

def int_plt(req):
    data=Plants.objects.all()[::-1]
    return render(req,'user/p_1.html',{'Plants':data})

def user_prfl(req):
    return render(req,'user/userprf.html')

def user_logout(req):
    req.session.flush()
    logout(req)
    return redirect(user_home)

def view_pro(req,pid):
    data=Plants.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})
def add_to_cart(req,pid):
    prdct=Plants.objects.get(pk=pid)
    try:

        user=User.objects.get(username=req.session['user'])
        data=Cart.objects.create(user=user,Plants=prdct)
        data.save()
        return redirect(view_cart)
    except:
        return redirect(m_login)

def view_cart(req):
    if 'user' in req.session:
        user=User.objects.get(username=req.session['user'])
        cart_dtls=Cart.objects.filter(user=user)
        return render(req,'user/cart.html',{'cart_dtls':cart_dtls})
    else:
        return redirect(m_login)




def add_catg(req):
    if req.method=='POST':
        name=req.POST['c_name']
        data=Category.objects.create(c_name=name)
        data.save()
        return redirect(add_catg)
    else:
        data=Category.objects.all()
        return render(req,'admin/add_catg.html',{'Category':data})

# def view_category(req):
#     data=Category.objects.all()
#     return render(req,'admin/add_catg.html',{'Category':data})