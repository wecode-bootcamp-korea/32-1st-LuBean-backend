from django.db import models
# from .models import *



# Create your models here.
class Cart(models.Model):
    amount  = models.IntegerField()
    # product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    class Meta:
        db_table = 'carts'
        
class ProductCart(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    cart    = models.ForeignKey('Cart', on_delete=models.CASCADE)
    class Meta:
        db_table = 'products_carts'