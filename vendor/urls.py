from django.urls import path
from . import views

app_name = "vendor"

urlpatterns = [
    path("vendors/", views.VendorListCreateAPIView.as_view(), name="vendor_list"),
    path("vendors/<int:pk>/", views.VendorDetailApiView.as_view(), name="Detail_View"),
    path(
        "vendors/<int:pk>/performance/",
        views.PerformanceDataView.as_view(),
        name="Performance",
    ),
]
