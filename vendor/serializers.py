from rest_framework import serializers
from .models import Vendor


class Vendor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "pk",
            "name",
            "contact_details",
            "address",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_respose_time",
            "fulfillment_rate",
        ]

    def get_name(self, obj):
        return self.name
