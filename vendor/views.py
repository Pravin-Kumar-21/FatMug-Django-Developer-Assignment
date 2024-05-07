from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, authentication
from .models import Vendor, HistoricalPerformance
from vendor.serializers import Vendor_Serializer, PerformanceSerializer
from rest_framework.response import responses, Response
from purchase.models import Purchase
from django.db.models import Avg
from datetime import timezone
from rest_framework import serializers, status
import datetime
from rest_framework.views import APIView
from django.db.models import Avg, Count


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = Vendor_Serializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class VendorDetailApiView(
    generics.RetrieveAPIView,
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Vendor.objects.all()
    serializer_class = Vendor_Serializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class PerformanceDataView(APIView):
    def get_vendor(self, pk):
        return get_object_or_404(Vendor, pk=pk)

    def get_historical_performance_instance(self, vendor):
        return HistoricalPerformance.objects.filter(vendor=vendor).first()

    def get(self, request, pk):
        vendor = self.get_vendor(pk)
        historical_performance_instance = self.get_historical_performance_instance(
            vendor
        )

        if not historical_performance_instance:

            return Response(
                {"error": "Historical performance not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PerformanceSerializer(historical_performance_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        vendor = self.get_vendor(pk)
        historical_performance_instance = self.get_historical_performance_instance(
            vendor
        )

        if historical_performance_instance:
            # Update existing historical performance instance
            historical_performance_instance.quality_rating_avg = get_quality_rating_avg(
                vendor
            )
            historical_performance_instance.fulfillment_rate = get_fulfillment_rate(
                vendor
            )
            # historical_performance_instance.average_response_time = (
            #     get_average_response_time(vendor)
            # )
            historical_performance_instance.on_time_delivery_rate = (
                get_on_time_delivery_rate(vendor)
            )
            historical_performance_instance.save()
        else:
            # Create new historical performance instance
            historical_performance_instance = HistoricalPerformance.objects.create(
                vendor=vendor,
                quality_rating_avg=get_quality_rating_avg(vendor),
                fulfillment_rate=get_fulfillment_rate(vendor),
                # average_response_time=get_average_response_time(vendor),
                on_time_delivery_rate=get_on_time_delivery_rate(vendor),
            )

        serializer = PerformanceSerializer(historical_performance_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#  Backend Logic Created
def get_on_time_delivery_rate(obj):
    completed_orders = Purchase.objects.filter(vendor=obj, status="completed")
    total_orders = Purchase.objects.filter(vendor=obj)
    on_time_delivery_rate = (
        completed_orders.filter(delivery_date__lte=timezone.now()).count()
        / completed_orders.count()
        * 100
        if completed_orders.count() > 0
        else 0
    )
    return on_time_delivery_rate


def get_quality_rating_avg(obj):
    purchases = Purchase.objects.filter(vendor=obj)
    if purchases.exists():
        total_rating = sum(
            purchase.quality_rating
            for purchase in purchases
            if purchase.quality_rating is not None
        )
        num_ratings = purchases.count()
        if num_ratings > 0:
            return total_rating / num_ratings

    return None


# def get_average_response_time(obj):
#     completed_orders = Purchase.objects.filter(vendor=obj, status="completed")
#     total_orders = Purchase.objects.filter(vendor=obj)

#     return response_times


def get_fulfillment_rate(obj):
    completed_orders = Purchase.objects.filter(vendor=obj, status="completed")
    total_orders = Purchase.objects.filter(vendor=obj)
    fulfilment_rate = (
        completed_orders.filter(status="completed").count() / total_orders.count() * 100
        if total_orders.count() > 0
        else 0
    )
    return fulfilment_rate
