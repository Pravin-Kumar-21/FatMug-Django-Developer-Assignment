from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Purchase
from purchase.serializers import Purchase_Serializer
from rest_framework.response import responses, Response
from rest_framework import generics


# Create your views here.
class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = Purchase_Serializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class PurchaseOrderDetail(
    generics.RetrieveAPIView,
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Purchase.objects.all()
    serializer_class = Purchase_Serializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
