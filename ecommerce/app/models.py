from django.db import models

# Create your models here.

class Plants(models.Model):
    p_id=models.TextField()
    name=models.TextField()
    p_catg=models.TextField()
    p_dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    img2=models.FileField()
