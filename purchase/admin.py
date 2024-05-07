from django.contrib import admin
from . import models as purchase_model

# Register your models here.

admin.site.register(purchase_model.Purchase)
# admin.site.register()
