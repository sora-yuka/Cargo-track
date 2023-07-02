from django.shortcuts import render

from rest_framework.viewsets import mixins, GenericViewSet

from applications.profiles.models import ShipperProfile
from applications.profiles.permissions import IsProfileOwner
from applications.profiles.serializers import ProfileSerializer

class ProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner]
    queryset = UserProfile.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset