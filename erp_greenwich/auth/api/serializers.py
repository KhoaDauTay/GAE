from casbin_adapter.models import CasbinRule
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ...users.models import Role
from ..models import Application, LogRequest, LogUri


class ApplicationSerializer(serializers.ModelSerializer):
    scopes = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = [
            "id",
            "name",
            "client_id",
            "redirect_uris",
            "client_type",
            "authorization_grant_type",
            "client_secret",
            "user",
            "scopes",
        ]

    @staticmethod
    def get_scopes(obj: Application):
        string_scopes = obj.scopes.split(" ")
        return string_scopes


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "name",
            "redirect_uris",
            "client_type",
            "authorization_grant_type",
            "scopes",
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["iss"] = "GAE"
        token["role"] = user.role.name.lower()
        # ...

        return token


class RoleSerializer(serializers.ModelSerializer):
    scopes = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ["id", "name", "description", "scopes"]

    @staticmethod
    def get_scopes(obj: Application):
        if obj.name == "ADMIN":
            rule_exist = (
                CasbinRule.objects.filter(ptype="p")
                .exclude(v0="admin")
                .values_list("v0", flat=True)
            )
            return list(rule_exist)
        rule_exist = CasbinRule.objects.filter(v0=obj.name.lower()).values_list(
            "v1", flat=True
        )
        return list(rule_exist)


class RuleUpdateSerializer(serializers.ModelSerializer):
    scopes = serializers.ListField(child=serializers.CharField(max_length=100))
    name = serializers.CharField(
        max_length=100, validators=[UniqueValidator(queryset=Role.objects.all())]
    )

    class Meta:
        model = Role
        fields = ["name", "description", "scopes"]

    def create(self, validated_data):
        scopes = validated_data.pop("scopes")
        role = Role.objects.create(**validated_data)
        with transaction.atomic():
            for rule in scopes:
                CasbinRule.objects.create(
                    ptype="g",
                    v0=f"{role.name.lower()}",
                    v1=f"{rule}",
                )
        return role

    def update(self, instance: Role, validated_data):
        # Update user
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.save()
        # Update role
        with transaction.atomic():
            rule_exist = CasbinRule.objects.filter(
                v0=instance.name.lower()
            ).values_list("v1", flat=True)
            rule_new = validated_data.get("scopes")
            # Change type to set:
            rule_exist = set(list(rule_exist))
            rule_new = set(rule_new)

            # Compare
            remove_rule = list(rule_exist.difference(rule_new))
            add_rule = list(rule_new.difference(rule_exist))

            CasbinRule.objects.filter(v1__in=remove_rule).delete()
            for rule in add_rule:
                CasbinRule.objects.create(
                    ptype="g",
                    v0=f"{instance.name.lower()}",
                    v1=f"{rule}",
                )
        return instance


class LogUriSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUri
        fields = ["uri", "sum_request"]


class LogRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRequest
        fields = "__all__"
