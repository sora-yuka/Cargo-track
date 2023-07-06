from rest_framework.permissions import BasePermission, SAFE_METHODS

from applications.job.models import Job
from applications.profiles.models import BaseProfile


class IsShipper(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated and BaseProfile.objects.get(user=request.user).shipper
        return request.user.is_authenticated and request.user == Job.objects.get(id=view.kwargs['pk']).owner
    
    
class IsCompanyOrCarrier(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and not BaseProfile.objects.get(user=request.user).shipper


class HistoryOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and not BaseProfile.objects.get(user=request.user).shipper:
            return True
    
        
        