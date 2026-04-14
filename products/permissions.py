from rest_framework.permissions import BasePermission


class MyPermissionClass(BasePermission):

    message = "You are not allowed to perform this action: MyPermissionClass "
    # It should return True otherwise it will return False
    def has_permission(self, request, view):
        return True
