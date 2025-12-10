from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Object-level permission to only allow owners of an object or Admin group members to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.user.groups.filter(name='Admin').exists() or request.user.is_superuser:
                return True
            return obj.owner == request.user
        return False
