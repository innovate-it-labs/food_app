

from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    """
    Allows access only to users with user_type == 'seller'.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'seller'
