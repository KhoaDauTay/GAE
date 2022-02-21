from rest_framework.permissions import BasePermission


class IsAuthenticatedOrClientCredentialPermission(BasePermission):
    def has_permission(self, request, view):
        if request.auth is None:
            return False
        grant_type = request.auth.application.get_authorization_grant_type_display()
        if request.user is None:
            if grant_type == "Client credentials":
                request.user = request.auth.application.user
                return True
            else:
                return False
        else:
            return True
