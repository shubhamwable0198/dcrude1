from django.db import models

# Create your models here.

class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=40)
    price = models.IntegerField()
    Delivery_Date = models.DateField()
