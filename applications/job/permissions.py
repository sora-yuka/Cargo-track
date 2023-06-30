from rest_framework.permissions import BasePermission, SAFE_METHODS


class ShipperOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return True
        
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user == obj.owner)