from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):  
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.JSONField(default=list)
    paid = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now=True)

    def get_total(self):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        return total

    def __str__(self):
        return f"Order {self.id}"