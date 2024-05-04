from django.db import models
from vendor import models as vendor_models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from django.utils import timezone
from datetime import timedelta


# Create your models here.
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
        help_text="Will be alloted automatically once the Order is  Created",
    )
    vendor = models.ForeignKey(
        vendor_models.Vendor,
        related_name="purchase",
        on_delete=models.SET_NULL,
        null=True,
    )
    order_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True,
        verbose_name="Order Date",
    )
    delivery_date = models.DateTimeField(
        blank=False,
        auto_now=False,
        auto_now_add=False,
        verbose_name="Expected Delivery Date",
    )
    quantity = models.IntegerField(blank=False, null=False)
    status = models.CharField(
        max_length=100,
        blank=False,
        choices=status_choices,
    )

    def json_data(self):
        vendor_name = self.vendor.name if self.vendor else None
        order_date_str = (
            self.order_date.isoformat()
            if self.order_date
            else timezone.now().date().isoformat()
        )

        return {
            "Order No": self.po_number,
            "Vendor Name": vendor_name,
            "Order Date": order_date_str,
            "Quantity": self.quantity,
        }

    items = models.JSONField(null=True, blank=True)
    quality_rating = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    issue_date = models.DateTimeField(
        blank=False,
        auto_now=True,
        auto_now_add=False,
    )
    acknowledgement_date = models.DateField(blank=True, auto_now_add=False, null=True)

    def __str__(self):
        return self.po_number

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = self.generate_unique_po_number()
        if not self.items:
            self.items = self.json_data()
        if self.order_date is not None and self.delivery_date is None:
            self.delivery_date = self.order_date + timedelta(days=6)
        super().save(*args, **kwargs)

    def generate_unique_po_number(self):
        return str(uuid.uuid4().hex[:6]).upper()
