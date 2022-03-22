import re

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from erp_greenwich.core.validation import APIValidationError
from erp_greenwich.users.models import Client, Role
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
        fields = [
            "id",
            "name",
            "email",
            "avatar",
            "role",
            "first_name",
            "last_name",
            "client",
        ]

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


class UserUpdateSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=20)
    client = ClientSerializer()

    class Meta:
        model = User
        fields = [
            "name",
            "role",
            "first_name",
            "last_name",
            "client",
        ]

    def update(self, instance: User, validated_data):
        instance.name = validated_data.get("name")
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")

        role = validated_data.pop("role")
        role_obj = Role.objects.get(name=role)
        instance.role = role_obj
        client_obj: Client = Client.objects.get(user=instance)
        client = validated_data.pop("client")
        client_obj.address = client.get("address")
        client_obj.city = client.get("city")
        client_obj.country = client.get("country")
        client_obj.postal_code = client.get("postal_code")
        client_obj.about_me = client.get("about_me")
        client_obj.save()
        return instance


class UserInviteSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    name = serializers.CharField(max_length=50)
    role = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "name", "role"]

    @staticmethod
    def validate_email(email):
        blacklist_domain = list(filter(bool, settings.EMAIL_BLACKLIST_DOMAIN))
        if len(blacklist_domain) > 0:
            blacklist_regex = re.compile(r"|".join(blacklist_domain))
            if blacklist_regex.search(email):
                raise APIValidationError({"email": "Email format is not supported"})
        return email

    def create(self, validated_data):
        data: dict = validated_data
        data["username"] = validated_data.get("email")
        data["email"] = validated_data.get("email")
        data["is_active"] = True
        role = validated_data.get("role")
        role_obj = Role.objects.get(name=role)
        if role_obj:
            data.pop("role")
        user = User.objects.create(**data)
        user.role = role_obj
        user.avatar = "avatar.png"
        user.set_password("khoa0305")
        client = Client.objects.create(
            user=user,
            address="06 Hoa Nam 3",
            city="Da Nang",
            country="Viet Nam",
            about_me="Example about me",
            postal_code="55000",
        )
        client.save()
        user.save(update_fields=["role", "password", "avatar"])
        return user
