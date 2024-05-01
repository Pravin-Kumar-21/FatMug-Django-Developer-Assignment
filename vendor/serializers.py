from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        feilds = [
            "name",
            "contact_details",
            "address",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_respose_time",
            "fulfillment_rate",
        ]
