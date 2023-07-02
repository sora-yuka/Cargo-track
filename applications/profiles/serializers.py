from rest_framework import serializers
from applications.profiles.models import ShipperProfile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = ShipperProfile
        fields = '__all__'
        