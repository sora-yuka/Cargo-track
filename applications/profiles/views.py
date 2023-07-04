from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from applications.feedback.views import FeedbackMixin

from applications.profiles.permissions import IsFeedbackOwner, IsProfileOwner
from applications.profiles.serializers import (
    BaseSerializer, ShipperSerializer, DriverSerializer, CompanyDriverSerializer, CompanySerializer
)
from applications.profiles.models import (
    BaseProfile, ShipperProfile, DriverProfile, CompanyDriverProfile, CompanyProfile
)


class BaseProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet, FeedbackMixin):
    permission_classes = [IsProfileOwner]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def get_permissions(self):
        if self.action == 'rating':
            return [IsFeedbackOwner()]
        return super().get_permissions()


class ShipperViewSet(BaseProfileViewSet):
    serializer_class = ShipperSerializer
    queryset = ShipperProfile.objects.all()
    
    
class DriverViewSet(BaseProfileViewSet):
    serializer_class = DriverSerializer
    queryset = DriverProfile.objects.all()
    
    
class CompanyDriverViewSet(BaseProfileViewSet):
    serializer_class = CompanyDriverSerializer
    queryset = CompanyDriverProfile.objects.all()
    
    
class CompanyViewSet(BaseProfileViewSet):
    serializer_class = CompanySerializer
    queryset = CompanyProfile.objects.all()
    
    
class ViewOtherProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = BaseSerializer
    queryset = BaseProfile.objects.all()
    permission_classes = [IsAuthenticated]