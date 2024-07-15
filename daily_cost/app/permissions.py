from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
