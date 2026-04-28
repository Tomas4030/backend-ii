from . import views
from django.urls import path

urlpatterns = [
    path("products/", views.product_list),
    path("orders/", views.order_list),
    path("add/<int:product_id>/", views.add_to_cart),
]