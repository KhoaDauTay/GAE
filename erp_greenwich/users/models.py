from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    ImageField,
    OneToOneField,
    TextField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from erp_greenwich.core.models.time_stamp import DateTimeModel


class Role(DateTimeModel):
    name = CharField(_("Name of Role"), max_length=255, unique=True)
    description = TextField(blank=True, default="")

    def __str__(self):
        return self.name


class User(AbstractUser, DateTimeModel):
    """Default user for ERP-GREENWICH."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(max_length=50, default="", blank=True)
    last_name = CharField(max_length=50, default="", blank=True)
    avatar = ImageField(null=True, blank=True)
    role = ForeignKey(
        Role,
        blank=True,
        null=True,
        on_delete=CASCADE,
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Client(DateTimeModel):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    address = CharField(max_length=100, default="", blank=True)
    city = CharField(max_length=50, default="", blank=True)
    country = CharField(max_length=50, default="", blank=True)
    postal_code = CharField(max_length=50, default="", blank=True)
    about_me = TextField(default="", blank=True)

    def __str__(self):
        return self.user.username
