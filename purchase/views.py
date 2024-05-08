from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Purchase
from purchase.serializers import Purchase_Serializer
from rest_framework.response import responses, Response
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from vendor.views import PerformanceDataView
from django.http import Http404
from .filters import PurchaseFilter


# Create your views here.
class ListCreateAPIView(generics.ListCreateAPIView):

    queryset = Purchase.objects.all()
    serializer_class = Purchase_Serializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class PurchaseOrderDetail(
    generics.RetrieveAPIView,
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Purchase.objects.all()
    serializer_class = Purchase_Serializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class AcknowledgePurchaseOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            purchase_order = get_object_or_404(Purchase, id=pk)
        except Http404:
            return Response(
                {"detail": "Purchase order not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if purchase_order.acknowledgement_date:
            return Response(
                {"detail": "Purchase order already acknowledged."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        purchase_order.acknowledgement_date = timezone.now()
        purchase_order.status = Purchase.completed
        purchase_order.save()

        try:
            performance_view = PerformanceDataView()
            response = performance_view.get(request, pk=purchase_order.vendor.pk)
            if response.status_code != status.HTTP_200_OK:
                return response  # Return performance data response if status is not OK

        except Exception as e:
            return Response(
                {"detail": f"Error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {"detail": "Purchase order acknowledged successfully."},
            status=status.HTTP_200_OK,
        )
