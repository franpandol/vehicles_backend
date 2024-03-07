from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vehicles.models import Vehicle

from .serializers import VehicleSerializer


class VehicleListEndpointTest(APITestCase):
    def setUp(self):
        # Create some Vehicle instances to test with
        Vehicle.objects.create(model="Model X", year=2020, vehicle_type=Vehicle.VehicleType.CARS, price=50000)
        Vehicle.objects.create(model="Model Y", year=2021, vehicle_type=Vehicle.VehicleType.PICKUPS, price=35000)
        Vehicle.objects.create(model="Model Z", year=2022, vehicle_type=Vehicle.VehicleType.SUVS, price=45000)

    def test_filter_by_vehicle_type(self):
        url = reverse("api:vehicles_list")
        response = self.client.get(url, {"vehicle_type": "CARS"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicles = Vehicle.objects.filter(vehicle_type="CARS")
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_ordering_by_price(self):
        url = reverse("api:vehicles_list")
        response = self.client.get(url, {"ordering": "price"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicles = Vehicle.objects.all().order_by("price")
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_ordering_by_year(self):
        url = reverse("api:vehicles_list")
        response = self.client.get(url, {"ordering": "-year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicles = Vehicle.objects.all().order_by("-year")
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data, serializer.data)
