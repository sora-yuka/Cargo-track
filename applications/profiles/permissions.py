from rest_framework.permissions import SAFE_METHODS, BasePermission

from applications.profiles.models import BaseProfile, CompanyProfile


class IsProfileOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user == obj.user)
    
    
class IsFeedbackOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            if not BaseProfile.objects.get(id=view.kwargs['pk']).shipper:
                try:
                    return request.user.is_authenticated and BaseProfile.objects.get(user=request.user).shipper
                except:
                    return 'Something went wrong'
        except:
            if CompanyProfile.objects.get(id=view.kwargs['pk']):
                try:
                    return request.user.is_authenticated and BaseProfile.objects.get(user=request.user).shipper
                except:
                    return 'Something went wrong'
                
