from django.contrib import admin
from . import models as performance_model

# Register your models here.

admin.site.register(performance_model.Performance)
