from django.db import models


class Review(models.Model):
    name=models.CharField(max_length=20)
    star = models.IntegerField(null=True)
    review=models.CharField(max_length=50)
    suggestion=models.CharField(max_length=50)
    


# Create your models here.
