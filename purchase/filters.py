import django_filters
from .models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    vendor = django_filters.NumberFilter(field_name="vendor__id")

    class Meta:
        model = Purchase
        fields = ["vendor"]  # Specify fields to filter on
