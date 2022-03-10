import re

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from erp_greenwich.core.validation import APIValidationError
from erp_greenwich.users.models import Client
from erp_greenwich.utils.client import get_client

User = get_user_model()


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["address", "city", "country", "about_me", "postal_code"]


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "name", "email", "role", "first_name", "last_name", "client"]

    @staticmethod
    def get_role(obj: User):
        return obj.role.name

    @staticmethod
    def get_client(obj: User):
        client: Client = get_client(obj)
        return ClientSerializer(client).data


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=32)
    confirm_password = serializers.CharField(min_length=8, max_length=32)
    name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password", "name"]

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise APIValidationError(
                {"password": "Password and confirm password must be the same!"}
            )
        return data

    @staticmethod
    def validate_email(email):
        blacklist_domain = list(filter(bool, settings.EMAIL_BLACKLIST_DOMAIN))
        if len(blacklist_domain) > 0:
            blacklist_regex = re.compile(r"|".join(blacklist_domain))
            if blacklist_regex.search(email):
                raise APIValidationError({"email": "Email format is not supported"})
        return email

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("confirm_password")
        validated_data["username"] = validated_data.get("email")
        validated_data["is_active"] = False
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save(update_fields=["password"])
        return user
