from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from api.serializers import VehicleSerializer
from vehicles.models import Vehicle


class VehicleListEndpoint(generics.ListAPIView):
    """
    Return a list of all **published** vehicles ordered by `order_weight`.
    The `order_weight` is used to determine the order of the vehicles in the list.
    The `order_weight` is set in the `Vehicle` model.


    The list can be filtered by `vehicle_type` and ordered by `price` and `year`.
    """

    queryset = Vehicle.published_objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "vehicle_type",
    ]
    ordering_fields = ["price", "year"]
    default_ordering = ["-order_weight"]
