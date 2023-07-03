from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet

from applications.profiles.permissions import IsProfileOwner
from applications.profiles.serializers import (
    ShipperSerializer, DriverSerializer, CompanyDriverSerializer, CompanySerializer
)
from applications.profiles.models import (
    ShipperProfile, DriverProfile, CompanyDriver, CompanyProfile
)


class BaseProfileViewSet(
        mixins.ListModelMixin, mixins.RetrieveModelMixin, 
        mixins.UpdateModelMixin, GenericViewSet
    ):
    permission_classes = [IsProfileOwner]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    

class ShipperViewSet(BaseProfileViewSet):
    serializer_class = ShipperSerializer
    queryset = ShipperProfile.objects.all()