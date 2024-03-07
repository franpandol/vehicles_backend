from django.db import models
from django.utils.translation import gettext_lazy as _

from vehicles.managers import PublishedVehiclesManger


class VehicleFeature(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="feature_images")
    show_on_gallery = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        CARS = "CARS", _("Autos")
        PICKUPS = "PICKUPS", _("Pickups y Comerciales")
        SUVS = "SUVS", _("Suvs y Crossovers")

    short_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vehicle_type = models.CharField(
        max_length=100,
        choices=VehicleType.choices,
        default=VehicleType.CARS,
    )
    image = models.ImageField(upload_to="vehicle_images", null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    features = models.ManyToManyField(VehicleFeature)
    order_weight = models.PositiveSmallIntegerField(default=0)  # Lower values will be shown first
    published = models.BooleanField(default=True)

    objects = models.Manager()
    published_objects = PublishedVehiclesManger()

    def __str__(self):
        return f"{self.year} {self.model}"
