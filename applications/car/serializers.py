from rest_framework import serializers
from applications.car.models import (
    CarBrand, CarType, CarDocument, CarEquipment, CarInfo
)


class CarBrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarBrand
        fields = "__all__"
        
    
class CarTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarType
        fields = "__all__"
        

class CarDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarDocument
        fields = "__all__"
        
    
class CarEquipmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarEquipment
        fields = "__all__"
        
        
class CarInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarInfo
        fields = "__all__"