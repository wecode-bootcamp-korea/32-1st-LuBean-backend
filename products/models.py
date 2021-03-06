from django.db import models

class Category(models.Model):
    name         = models.CharField(max_length=45)
    menu         = models.ForeignKey('Menu', on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=45, blank=True)
    sub_detail   = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = 'categories'
        
class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'menus'
        
class Product(models.Model):
    korean_name       = models.CharField(max_length=55)
    english_name      = models.CharField(max_length=55)
    country_name      = models.CharField(max_length=45, blank=True)
    weight            = models.CharField(max_length=45, blank=True)
    label             = models.CharField(max_length=45, blank=True)
    price             = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category          = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    detail            = models.TextField(blank=True)
    country           = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'products'

class Country(models.Model):
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'countries'

class Image(models.Model):
    image_url  = models.CharField(max_length=2000, blank=True)
    image_info = models.CharField(max_length=200, blank=True)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
        
class ProductCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products_categories'