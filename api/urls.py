from django.urls import path

from api.views import VehicleListEndpoint

urlpatterns = [
    path("vehicles/", VehicleListEndpoint.as_view(), name="list"),
]
