from rest_framework import serializers
from applications.profiles.models import ShipperProfile, DriverProfile


class ShipperSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShipperProfile
        fields = "__all__"
        

class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DriverProfile
        fields = "__all__"