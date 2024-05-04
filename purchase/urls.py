from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    path(
        "purchase_orders/",
        views.ListCreateAPIView.as_view(),
        name="order_list",
    ),
    path(
        "purchase_orders/<int:pk>/",
        views.PurchaseOrderDetail.as_view(),
        name="detail_purchase",
    ),
]
