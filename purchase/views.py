from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Purchase
from purchase.serializers import Purchase_Serializer
from rest_framework.response import responses, Response


# Create your views here.
@api_view(["GET"])
def purchase_order_list(request, *args, **kwargs):
    instance = Purchase.objects.all()
    if instance:
        data = Purchase_Serializer(instance, many=True).data
    return Response(data)
