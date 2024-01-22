from django.db import models
from django.db.models import CharField
from oauth2_provider.models import (
    AbstractAccessToken,
    AbstractApplication,
    AbstractRefreshToken,
)


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


class LogRequest(models.Model):
    year = CharField(max_length=100, default="", blank=True)
    january = models.IntegerField(default=0, blank=True)
    february = models.IntegerField(default=0, blank=True)
    march = models.IntegerField(default=0, blank=True)
    april = models.IntegerField(default=0, blank=True)
    may = models.IntegerField(default=0, blank=True)
    june = models.IntegerField(default=0, blank=True)
    july = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.year


class LogUri(models.Model):
    uri = CharField(max_length=400, default="", blank=True)
    january = models.IntegerField(default=0, blank=True)
    february = models.IntegerField(default=0, blank=True)
    march = models.IntegerField(default=0, blank=True)
    april = models.IntegerField(default=0, blank=True)
    may = models.IntegerField(default=0, blank=True)
    june = models.IntegerField(default=0, blank=True)
    july = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.uri

    @property
    def sum_request(self):
        sum_month = (
            self.january
            + self.february
            + self.march
            + self.april
            + self.may
            + self.june
            + self.july
        )
        return sum_month
