from rest_framework import serializers
from .models import Purchase


class Purchase_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = [
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgement_date",
        ]
