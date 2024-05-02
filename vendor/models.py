from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    contact_details = models.TextField(max_length=100, blank=False, null=False)
    address = models.TextField(max_length=100, blank=False, null=False)
    on_time_delivery_rate = models.FloatField(
        null=False, blank=False, verbose_name="On time delivery Percentage"
    )
    quality_rating_avg = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        verbose_name="Product Quality",
    )
    average_respose_time = models.FloatField(
        blank=False, null=False, verbose_name="Acknowledge time for orders"
    )
    fulfillment_rate = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Order fulfillment rate",
    )

    def __str__(self) -> str:
        return self.name


class Performance(models.Model):
    vendor = models.ForeignKey(
        Vendor,
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
