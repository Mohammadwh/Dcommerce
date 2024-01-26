import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Customers(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = False
    telephone = models.CharField(max_length=100)

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='address')
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    postal_code = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    mobile = models.CharField(max_length=100,blank=True)

