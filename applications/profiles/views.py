from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from applications.feedback.views import FeedbackMixin

from applications.profiles.permissions import IsFeedbackOwner, IsProfileOwner
from applications.profiles.serializers import (
    ShipperSerializer, DriverSerializer, CompanyDriverSerializer, CompanySerializer
)
from applications.profiles.models import (
    ShipperProfile, DriverProfile, CompanyDriverProfile, CompanyProfile
)





class ShipperViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = ShipperSerializer
    queryset = ShipperProfile.objects.all()
    permission_classes = [IsProfileOwner]
    
    
    
    
class DriverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet, FeedbackMixin):
    serializer_class = DriverSerializer
    queryset = DriverProfile.objects.all()
    permission_classes = [IsProfileOwner]
    
    def get_permissions(self):
        if self.action == 'rating':
            return [IsFeedbackOwner()]
        return super().get_permissions()
    
    
class CompanyDriverViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = CompanyDriverSerializer
    queryset = CompanyDriverProfile.objects.all()
    permission_classes = [IsProfileOwner]
    
    
class CompanyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet, FeedbackMixin):
    serializer_class = CompanySerializer
    queryset = CompanyProfile.objects.all()
    permission_classes = [IsProfileOwner]
    
    
    def get_permissions(self):
        if self.action == 'rating':
            return [IsFeedbackOwner()]
        return super().get_permissions()