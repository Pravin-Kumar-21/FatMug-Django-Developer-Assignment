from django.contrib import admin

# Register your models here.
from . import models as Vendor_models

admin.site.register(Vendor_models.Vendor)
admin.site.register(Vendor_models.HistoricalPerformance)
