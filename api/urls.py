from django.urls import path

from api.views import VehicleListEndpoint

app_name = "api"

urlpatterns = [
    path("vehicles/", VehicleListEndpoint.as_view(), name="vehicles_list"),
]
