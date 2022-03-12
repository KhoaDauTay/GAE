from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from erp_greenwich.auth.api.views import ApplicationViewSet
from erp_greenwich.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register("users", UserViewSet, basename="users")
router.register("applications", ApplicationViewSet, basename="applications")

app_name = "api"
urlpatterns = router.urls
