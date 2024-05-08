from rest_framework import serializers
from .models import Vendor
from purchase.models import Purchase
from .models import HistoricalPerformance
from datetime import timezone


class Vendor_Serializer(serializers.ModelSerializer):
    vendor_code = serializers.CharField(read_only=True)

    class Meta:
        model = Vendor
        fields = [
            "pk",
            "name",
            "vendor_code",
            "contact_details",
            "address",
        ]

    def get_name(self, obj):
        return self.name


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = [
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
