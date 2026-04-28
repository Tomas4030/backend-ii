from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.models import User
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products}) 

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # cria ou usa uma order simples
    order, created = Order.objects.get_or_create(
        user=User.objects.first(),  # simplificado (para escola)
        paid=False
    )

    cart = order.cart

    # ver se já existe produto
    found = False
    for item in cart:
        if item["product_id"] == product.id:
            item["quantity"] += 1
            found = True

    if not found:
        cart.append({
            "product_id": product.id,
            "name": product.name,
            "price": float(product.price),
            "quantity": 1
        })

    order.cart = cart
    order.save()

    return redirect("/products/")
