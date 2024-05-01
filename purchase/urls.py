from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [path("purchase_orders/", views.purchase_order_list, name="order_list")]
