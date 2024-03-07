from django.contrib import admin

from vehicles.models import Vehicle, VehicleFeature


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "price", "vehicle_type", "published")
    search_fields = (
        "short_name",
        "full_name",
        "model",
    )
    list_filter = ("vehicle_type", "model", "year")
    ordering = ("-id",)
    actions = ["publish_vehicle"]

    def publish_vehicle(self, request, queryset):
        queryset.update(published=True)
        self.message_user(request, "Selected vehicles have been published.")

    publish_vehicle.short_description = "Publish selected vehicles"

    def unpublish_vehicle(self, request, queryset):
        queryset.update(published=False)
        self.message_user(request, "Selected vehicles have been unpublished.")

    unpublish_vehicle.short_description = "Unpublish selected vehicles"


admin.site.register(Vehicle, VehicleAdmin)

admin.site.register(VehicleFeature)
