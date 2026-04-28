from django.contrib import admin
from .models import Product, Order
import json

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "paid", "update_time", "total")

    def total(self, obj):
        return obj.get_total()

    readonly_fields = ("pretty_cart",)

    def pretty_cart(self, obj):
        return json.dumps(obj.cart, indent=2)