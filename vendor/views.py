from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, authentication
from .models import Vendor
from vendor.serializers import Vendor_Serializer
from rest_framework.response import responses, Response


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = Vendor_Serializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class VendorDetailApiView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = Vendor_Serializer
    lookup_field = "pk"
