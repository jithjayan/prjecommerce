from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    c_name=models.TextField()
class Plants(models.Model):
    p_id=models.TextField()
    name=models.TextField()
    p_catg=models.TextField()
    p_dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    img2=models.FileField()
    catg=models.ForeignKey(Category,on_delete=models.CASCADE)
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Plants=models.ForeignKey(Plants,on_delete=models.CASCADE)
    