from rest_framework_simplejwt.views import TokenObtainPairView

from erp_greenwich.auth.api.serializers import (
    ApplicationSerializer,
    MyTokenObtainPairSerializer,
)
from erp_greenwich.core.views.base_view import BaseViewSet


class ApplicationViewSet(BaseViewSet):
    serializer_class = ApplicationSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
