from django.db import models

from vendor.models import Vendor
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from django.utils import timezone
from datetime import timedelta


class Purchase(models.Model):
    pending = "Pending"
    completed = "Completed"
    cancelled = "Cancelled"
    status_choices = (
        (pending, "Pending"),
        (completed, "Completed"),
        (cancelled, "Cancelled"),
    )
    po_number = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Unique Product Order No",
        help_text="Will be alloted automatically once the Order is Created",
    )
    vendor = models.ForeignKey(
        Vendor,
        related_name="purchase",
        on_delete=models.SET_NULL,
        null=True,
    )
    order_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=False,
        verbose_name="Order Date",
    )
    delivery_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Expected Delivery Date",
    )
    quantity = models.IntegerField(blank=False, null=False)
    status = models.CharField(
        default=pending,
        max_length=100,
        blank=True,
        choices=status_choices,
    )
    items = models.JSONField(null=True, blank=True)
    quality_rating = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    issue_date = models.DateTimeField(
        blank=False,
        auto_now=True,
    )
    acknowledgement_date = models.DateTimeField(
        blank=True, null=True, auto_now_add=True
    )

    def __str__(self):
        return self.po_number

    def save(self, *args, **kwargs):
        if not self.pk:
            self.po_number = self.generate_unique_po_number()
            self.delivery_date = self.order_date + timedelta(days=3)
            self.items = self.json_data()
            if self.status != self.completed:
                self.status = self.completed
                self.performance.update_on_time_delivery_rate()
                self.acknowledgement_date = timezone.now()
                self.performance.update_average_response_time()
        super().save(*args, **kwargs)

    def json_data(self):
        vendor_name = self.vendor.name if self.vendor else None
        order_date_str = (
            self.order_date.date().isoformat()
        )  # Format order_date as ISO date
        return {
            "Order No": self.po_number,
            "Vendor Name": vendor_name,
            "Order Date": order_date_str,
            "Quantity": self.quantity,
        }

    def generate_unique_po_number(self):
        return str(uuid.uuid4().hex[:6]).upper()
