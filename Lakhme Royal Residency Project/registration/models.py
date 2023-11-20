from django.db import models

class regi(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    adhar = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

# Create your models here.
