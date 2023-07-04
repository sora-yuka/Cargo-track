from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from applications.car.models import (
    CarBrand, CarType, CarDocument, CarEquipment, CarInfo
)
from applications.car.serializers import (
    CarBrandSerializer, CarTypeSerializer, CarDocumentSerializer, CarEquipmentSerializer, CarInfoSerializer
)


class CarBrandViewSet(ModelViewSet):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.all()
    permission_classes = [IsAdminUser]
    
    
class CarTypeViewSet(ModelViewSet):
    serializer_class = CarTypeSerializer
    queryset = CarType.objects.all()
    permission_classes = [IsAdminUser]
    
    
class CarDocumentViewSet(ModelViewSet):
    serializer_class = CarDocumentSerializer
    queryset = CarDocument.objects.all()
    permission_classes = [IsAdminUser]
    
    
class CarEquipmentViewSet(ModelViewSet):
    serializer_class = CarEquipmentSerializer
    queryset = CarEquipment.objects.all()
    permission_classes = [IsAdminUser]
    
    
class CarInfoViewSet(ModelViewSet):
    serializer_class = CarInfoSerializer
    queryset = CarInfo.objects.all()
    permission_classes = [IsAdminUser]