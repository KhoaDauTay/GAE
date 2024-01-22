from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from erp_greenwich.auth.api.views import (
    ApplicationViewSet,
    LogRequestViewSet,
    LogUriViewSet,
    RoleViewSet,
)
from erp_greenwich.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register("users", UserViewSet, basename="users")
router.register("applications", ApplicationViewSet, basename="applications")
router.register("roles", RoleViewSet, basename="roles")
router.register("uris", LogUriViewSet, basename="uris")
router.register("requests", LogRequestViewSet, basename="requests")

app_name = "api"
urlpatterns = router.urls
