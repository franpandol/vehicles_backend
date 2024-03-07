from rest_framework import serializers

from vehicles.models import Vehicle, VehicleFeature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFeature
        fields = ("title", "description", "show_on_gallery", "image", "featured")


class VehicleSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Vehicle
        fields = ("id", "short_name", "full_name", "model", "year", "price", "vehicle_type", "features")
