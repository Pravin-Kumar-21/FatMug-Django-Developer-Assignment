from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta
import uuid

# from purchase.models import Purchase


class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    contact_details = models.TextField(max_length=100, blank=False, null=False)
    address = models.TextField(max_length=100, blank=False, null=False)
    vendor_code = models.CharField(max_length=20, unique=True, blank=True)
    on_time_delivery_rate = models.FloatField(
        null=True, blank=True, verbose_name="On time delivery Percentage"
    )
    quality_rating_avg = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        verbose_name="Product Quality",
    )
    average_respose_time = models.FloatField(
        blank=True, null=True, verbose_name="Acknowledge time for orders"
    )
    fulfillment_rate = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Order fulfillment rate",
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = self.generate_unique_vendor_code()
        super().save(*args, **kwargs)

    def generate_unique_vendor_code(self):
        short = self.name[:5]
        return short + str(uuid.uuid4().hex[:6]).upper()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    quality_rating_avg = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
