import logging

import casbin
from django.conf import settings
from django.core.exceptions import PermissionDenied
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import BasePermission, IsAuthenticated

from erp_greenwich.auth.models import AccessToken
from erp_greenwich.utils.import_class import import_class

log = logging.getLogger("oauth2_provider")


class TokenPermissionWithAction(BasePermission):
    def __init__(self):
        # Initialize the Casbin enforcer, executed only on once.
        class_adapter = import_class(settings.CASBIN_ADAPTER)
        adapter = class_adapter()
        e = casbin.Enforcer(settings.CASBIN_MODEL, adapter)
        self.enforcer = e

    def has_permission(self, request, view):
        token: AccessToken = request.auth
        if not token:
            return False

        if hasattr(token, "scope"):  # OAuth 2

            scope = getattr(view, "get_scopes_with_actions")
            if token.is_valid([scope]) and self.casbin_authorize(request, scope):
                return True
            return False

        assert False, (
            "TokenRequirements requires the"
            "`oauth2_provider.rest_framework.OAuth2Authentication` authentication "
            "class to be used."
        )

    def casbin_authorize(self, request, scope):
        # Check the permission for each request.
        if not self.check_permission(request, scope):
            # Not authorized, return HTTP 403 error.
            self.require_permission()
        # Permission passed, go to next module.
        return True

    def check_permission(self, request, scope):
        # Customize it based on your authentication method.
        role = request.user.role
        # RBAC
        sub = role.lower()
        obj = scope
        act = request.method
        return self.enforcer.enforce(sub, obj, act)

    def require_permission(
        self,
    ):
        raise PermissionDenied("Your role can not access resource")


class IsAuthenticatedOrTokenPermissionWithAction(BasePermission):
    """
    The user is authenticated using some backend or the token has the right scope
    This only returns True if the user is authenticated, but not using a token
    or using a token, and the token has the correct scope.

    This is usefull when combined with the DjangoModelPermissions to allow people browse
    the browsable api's if they log in using the a non token bassed middleware,
    and let them access the api's using a rest client with a token
    """

    def has_permission(self, request, view):
        is_authenticated = IsAuthenticated().has_permission(request, view)
        oauth2authenticated = False
        if is_authenticated:
            oauth2authenticated = isinstance(
                request.successful_authenticator, OAuth2Authentication
            )

        token_has_scope = TokenPermissionWithAction()
        return (
            is_authenticated and not oauth2authenticated
        ) or token_has_scope.has_permission(request, view)
