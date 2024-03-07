from rest_framework import routers

from api.views import VehicleViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"vehicles", VehicleViewSet, basename="vehicles")
urlpatterns = router.urls
