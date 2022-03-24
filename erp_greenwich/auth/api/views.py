from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from erp_greenwich.auth.api.serializers import (
    ApplicationCreateSerializer,
    ApplicationSerializer,
    MyTokenObtainPairSerializer,
    RoleSerializer,
    RuleUpdateSerializer,
)
from erp_greenwich.core.views.base_view import BaseViewSet
from erp_greenwich.utils.get_action import read_file_json


class ApplicationViewSet(BaseViewSet):
    serializer_class = ApplicationSerializer
    serializer_map = {
        "retrieve": ApplicationSerializer,
        "update": ApplicationCreateSerializer,
        "create": ApplicationCreateSerializer,
    }

    @action(detail=False, url_name="get_roles", url_path="get-roles", methods=["GET"])
    def get_roles(self, request, *args, **kwargs):
        scopes_path = settings.GROUP_SCOPES_JSON_PATH
        scopes: dict = read_file_json(scopes_path)
        return Response(scopes, status=200)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RoleViewSet(BaseViewSet):
    serializer_class = RoleSerializer
    serializer_map = {
        "update": RuleUpdateSerializer,
    }
