from django.db import models


class Product(models.Model):
    Name=models.CharField(max_length=50)
    Disc=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=50)


# Create your models here.
