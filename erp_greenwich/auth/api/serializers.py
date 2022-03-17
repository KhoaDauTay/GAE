from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import Application


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


# Create your views here.
