from rest_framework_simplejwt.views import TokenObtainPairView

from erp_greenwich.auth.api.serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    MyTokenObtainPairSerializer,
)
from erp_greenwich.core.views.base_view import BaseViewSet


class ApplicationViewSet(BaseViewSet):
    serializer_class = ApplicationSerializer
    serializer_map = {
        "retrieve": ApplicationSerializer,
        "update": ApplicationCreateSerializer,
        "create": ApplicationCreateSerializer,
    }


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
