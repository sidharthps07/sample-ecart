from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=3000)


class Offers(models.Model):
    code = models.CharField(max_length=300)
    discount = models.CharField(max_length=300)
