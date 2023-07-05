from rest_framework import serializers
from applications.car.models import CarInfo

        
class CarInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarInfo
        fields = "__all__"