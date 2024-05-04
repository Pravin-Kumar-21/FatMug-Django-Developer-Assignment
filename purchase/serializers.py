from rest_framework import serializers
from .models import Purchase


class Purchase_Serializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(read_only=True)
    acknowledgement_date = serializers.DateTimeField(read_only=True)
    po_number = serializers.CharField(read_only=True)
    items = serializers.JSONField(read_only=True)
    delivery_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Purchase
        fields = [
            "pk",
            "po_number",
            "vendor",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "order_date",
            "acknowledgement_date",
        ]
