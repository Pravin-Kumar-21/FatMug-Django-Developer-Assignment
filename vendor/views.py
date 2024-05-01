from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, authentication
from .models import Vendor
from vendor.serializers import VendorSerializer
from rest_framework.response import responses, Response


@api_view(["GET"])
def api_vendor_list(request, *args, **kwargs):
    instance = Vendor.objects.all()
    data = {}
    if instance:
        data = VendorSerializer(instance).data
    return Response(data)
