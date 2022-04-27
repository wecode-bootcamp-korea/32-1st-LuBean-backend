from django.db import models

class Cart(models.Model):
    quantity       = models.PositiveIntegerField()
    user           = models.ForeignKey("users.User", on_delete=models.CASCADE)
    order          = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    price          = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    class Meta:
        db_table = 'carts'
        
class Order(models.Model):
    user         = models.ForeignKey("users.User", on_delete=models.CASCADE)
    address      = models.CharField(max_length=500, null=True)
    order_status = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        
class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "order_status"