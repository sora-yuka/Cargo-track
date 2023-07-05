# from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from applications.car.models import CarInfo
from applications.car.serializers import CarInfoSerializer

    
class CarInfoViewSet(ModelViewSet):
    serializer_class = CarInfoSerializer
    queryset = CarInfo.objects.all()
    # permission_classes = []