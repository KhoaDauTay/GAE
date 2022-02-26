from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, ForeignKey, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from erp_greenwich.core.models.time_stamp import DateTimeModel


class Role(DateTimeModel):
    name = CharField(_("Name of Role"), max_length=255, unique=True)
    description = TextField(blank=True, default="")

    def count_role(self):
        roles: list = self.objects.all()
        return len(roles)


class User(AbstractUser, DateTimeModel):
    """Default user for ERP-GREENWICH."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
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
