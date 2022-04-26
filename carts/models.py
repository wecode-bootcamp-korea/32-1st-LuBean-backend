from django.db import models

# Create your models here.
class Cart(models.Model):
    amount  = models.IntegerField()
    users   = models.OneToOneField('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'carts'
class ProductCart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart    = models.ForeignKey('Cart', on_delete=models.CASCADE)
    class Meta:
        db_table = 'products_carts'