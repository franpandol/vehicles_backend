from django.db import models


class PublishedVehiclesManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)
