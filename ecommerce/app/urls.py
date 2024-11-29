from django.urls import path
from . import views


urlpatterns=[
    path('',views.m_login),
    path('reg',views.reg),
    path('admin_home',views.admin_home),
    path('user_home',views.user_home)



]