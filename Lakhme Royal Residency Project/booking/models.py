from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    room_type = models.CharField(
        max_length=10,
        choices=[
            ('standard', 'Standard Room'),
            ('deluxe', 'Deluxe Room'),
            ('suite', 'Suite'),
        ]
    )




    
# Create your models here.
