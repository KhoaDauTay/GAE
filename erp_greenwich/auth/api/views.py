from casbin_adapter.models import CasbinRule
from django.conf import settings
from django.db import transaction
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
from erp_greenwich.users.models import Role
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
        "add_rule": RuleUpdateSerializer,
    }

    @action(detail=True, url_name="add_rule", url_path="add-rule", methods=["POST"])
    def add_rule(
        self,
        request,
        pk=None,
        *args,
        **kwargs,
    ):
        role: Role = self.get_object()
        data: dict = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                rule_exist = CasbinRule.objects.filter(
                    v0=role.name.lower()
                ).values_list("v1", flat=True)
                rule_new = serializer.validated_data.get("scopes")
                # Change type to set:
                rule_exist = set(list(rule_exist))
                rule_new = set(rule_new)

                # Compare
                remove_rule = list(rule_exist.difference(rule_new))
                add_rule = list(rule_new.difference(rule_exist))

                CasbinRule.objects.filter(v1__in=remove_rule).delete()
                for rule in add_rule:
                    key_split = rule.split(":")
                    basename = key_split[0]
                    action = key_split[1]
                    CasbinRule.objects.create(
                        ptype="g",
                        v0=f"{role.name.lower()}",
                        v1=f"{basename}",
                        v2=f"{action}",
                    )
            return Response(status=201, data={"message": "Update role successfully"})
        return self.failure_response()
