from django.db import models
from oauth2_provider.models import AbstractApplication, AbstractAccessToken, AbstractRefreshToken, AbstractIDToken, \
    AbstractGrant


class Application(AbstractApplication):
    scopes = models.TextField(blank=True, null=True)

    class Meta(AbstractApplication.Meta):
        swappable = "OAUTH2_PROVIDER_APPLICATION_MODEL"


class AccessToken(AbstractAccessToken):
    token = models.CharField(
        max_length=4096,
        unique=True,
    )

    class Meta(AbstractAccessToken.Meta):
        swappable = "OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL"


class RefreshToken(AbstractRefreshToken):
    """
    extend the AccessToken model with the external introspection server response
    """
    class Meta(AbstractRefreshToken.Meta):
        swappable = "OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL"
