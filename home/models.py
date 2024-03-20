from django.db import models


# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True,max_length=50)
    phone = models.DecimalField(decimal_places=0,max_digits=10)
