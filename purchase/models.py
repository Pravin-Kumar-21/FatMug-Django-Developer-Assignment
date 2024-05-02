from django.db import models
from vendor import models as vendor_models
from django.core.validators import MinValueValidator, MaxValueValidator


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
        max_length=100, null=False, verbose_name="Unique Product Order No"
    )
    vendor = models.ForeignKey(
        vendor_models.Vendor, related_name="purchase", on_delete=models.CASCADE
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
        auto_now=True,
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
        return {
            "Order No": self.po_number,
            "Vendor Name": self.vendor,
            "Order Date": self.order_date,
            "Quantity": self.quantity,
            "Delivery Date": self.delivery_date,
        }

    items = models.JSONField(default=dict, null=True, blank=True)
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
