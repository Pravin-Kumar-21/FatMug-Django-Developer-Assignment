from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, authentication
from .models import Vendor, HistoricalPerformance
from vendor.serializers import Vendor_Serializer, PerformanceSerializer
from rest_framework.response import responses, Response
from purchase.models import Purchase
from django.db.models import Avg
from django.utils import timezone
from rest_framework import serializers, status
from datetime import timedelta
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
            historical_performance_instance = HistoricalPerformance.objects.create(
                vendor=vendor,
                quality_rating_avg=get_quality_rating_avg(vendor),
                fulfillment_rate=get_fulfillment_rate(vendor),
                # average_response_time=get_average_response_time(vendor),
                on_time_delivery_rate=get_on_time_delivery_rate(vendor),
            )
        if historical_performance_instance:
            # Update existing historical performance instance
            historical_performance_instance.quality_rating_avg = get_quality_rating_avg(
                vendor
            )
            historical_performance_instance.fulfillment_rate = get_fulfillment_rate(
                vendor
            )
            historical_performance_instance.average_response_time = (
                get_average_response_time(vendor)
            )
            historical_performance_instance.on_time_delivery_rate = (
                get_on_time_delivery_rate(vendor)
            )
            historical_performance_instance.save()
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
            historical_performance_instance.average_response_time = (
                get_average_response_time(vendor)
            )
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

    # Query completed purchase orders for the specified vendor
    completed_orders = Purchase.objects.filter(vendor=obj, status=Purchase.completed)

    if completed_orders.exists():
        on_time_deliveries = completed_orders.filter(
            delivery_date__gte=timezone.now()
        ).count()
        on_time_delivery_rate = (on_time_deliveries / completed_orders.count()) * 100
    else:
        on_time_delivery_rate = 0
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


def get_average_response_time(obj):
    # Query acknowledged purchase orders for the specified vendor
    acknowledged_orders = Purchase.objects.filter(vendor=obj, status=Purchase.completed)

    if acknowledged_orders.exists():
        total_response_time = timedelta()  # Initialize total response time
        num_orders = 0

        for order in acknowledged_orders:
            if order.issue_date and order.acknowledgement_date:
                response_time = order.acknowledgement_date - order.issue_date
                total_response_time += response_time
                num_orders += 1

        if num_orders > 0:
            average_response_time = total_response_time / num_orders
            return (
                average_response_time.total_seconds() / 3600
            )  # Return average in hours
    else:
        return None  # Return None if no acknowledged orders exist


def get_fulfillment_rate(obj):
    completed_orders = Purchase.objects.filter(vendor=obj, status=Purchase.completed)
    total_orders = Purchase.objects.filter(vendor=obj)
    fulfilment_rate = (
        completed_orders.filter(status=Purchase.completed).count()
        / total_orders.count()
        * 100
        if total_orders.count() > 0
        else 0
    )
    return fulfilment_rate
