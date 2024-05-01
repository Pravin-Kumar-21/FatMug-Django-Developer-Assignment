from django.db import models
from vendor import models as vendor_models


class Performance(models.Model):
    vendor = models.ForeignKey(
        vendor_models.Vendor,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(
        auto_now=True, auto_now_add=False, verbose_name="Performance Record"
    )
    on_time_delivery_rate = models.FloatField(
        null=False, blank=False, verbose_name="On Time Delivery Percentage"
    )
    quality_rating_avg = models.FloatField(
        null=False, blank=False, verbose_name="Quality Average Rating"
    )
    average_response_time = models.FloatField(
        null=False, blank=False, verbose_name="Vendor Response Time"
    )
    fulfillment_rate = models.FloatField(
        null=False, blank=False, verbose_name="Order Fulfillment Rate"
    )
