import casbin
from django.conf import settings
from django.core.exceptions import PermissionDenied

from erp_greenwich.utils.import_class import import_class


class CasbinMiddleware:
    """
    Casbin middleware.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Initialize the Casbin enforcer, executed only on once.
        class_adapter = import_class(settings.CASBIN_ADAPTER)
        adapter = class_adapter(settings.CASBIN_ADAPTER_ARGS)
        e = casbin.Enforcer(settings.CASBIN_MODEL, adapter)
        self.enforcer = e

    def __call__(self, request):
        # Check the permission for each request.
        if not self.check_permission(request):
            # Not authorized, return HTTP 403 error.
            self.require_permission()

        # Permission passed, go to next module.
        response = self.get_response(request)
        return response

    def check_permission(self, request):
        # Customize it based on your authentication method.
        if request.user.is_authenticated:
            role = request.user.role.name
        else:
            role = "anonymous"
        sub = role.lower()
        obj = request.path
        act = request.method
        return self.enforcer.enforce(sub, obj, act)

    def require_permission(
        self,
    ):
        raise PermissionDenied
