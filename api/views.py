from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from api.serializers import VehicleSerializer
from vehicles.models import Vehicle


class VehicleListEndpoint(generics.ListAPIView):
    queryset = Vehicle.published_objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "vehicle_type",
    ]
    ordering_fields = ["price", "year"]
    default_ordering = ["-order_weight"]
