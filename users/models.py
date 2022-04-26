from django.db import models
# from .models import *

# Create your models here.
class User(models.Model):
    username     = models.CharField(max_length=45)
    email        = models.CharField(max_length=200, unique=True)
    password     = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=30)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    # cart = models.OneToOneField('carts.Cart', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'users'
        
        