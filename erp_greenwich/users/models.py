from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from erp_greenwich.core.models.time_stamp import DateTimeModel
from erp_greenwich.utils.enum import Role


class User(AbstractUser, DateTimeModel):
    """Default user for ERP-GREENWICH."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in Role],  # Choices is a list of Tuple,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
