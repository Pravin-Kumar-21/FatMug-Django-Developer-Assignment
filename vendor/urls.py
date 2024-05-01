from django.urls import path
from . import views

app_name = "vendor"

urlpatterns = [
    path("vendors/", views.api_vendor_list, name="vendor_list"),
]
