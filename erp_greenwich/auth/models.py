from django.db import models
from oauth2_provider.models import AbstractApplication


class GreenwichApplication(AbstractApplication):
    scopes = models.TextField(blank=True, null=True)


class Role(models.Model):
    pass
