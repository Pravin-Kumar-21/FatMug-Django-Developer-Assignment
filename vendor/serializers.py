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

    def get_quality_rating_avg(self, obj):
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
