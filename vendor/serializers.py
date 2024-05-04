from rest_framework import serializers
from .models import Vendor


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
            # "quality_rating_avg",
            # "average_respose_time",
            # "fulfillment_rate",
        ]

    def get_name(self, obj):
        return self.name
