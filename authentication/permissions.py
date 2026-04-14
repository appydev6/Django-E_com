from rest_framework.permissions import BasePermission
from authentication.models import User

class IsAuthenticatedAndActiveUser(BasePermission):

    message = "Invalid Token Or User"

    def has_permission(self, request, view): # type: ignore
        request_user = request.user
        return isinstance(request_user, User) and (request_user.is_active == True)
