import pytest
from django.urls import resolve, reverse

from erp_greenwich.users.models import User

pytestmark = pytest.mark.django_db


def test_user_detail(user: User):
    assert (
        reverse("api:users-detail", kwargs={"id": user.id}) == f"/api/users/{user.id}"
    )
    assert resolve(f"/api/users/{user.id}").view_name == "api:users-detail"


def test_user_list():
    assert reverse("api:users-list") == "/api/users"
    assert resolve("/api/users").view_name == "api:users-list"


def test_user_me():
    assert reverse("api:users-me") == "/api/users/me"
    assert resolve("/api/users/me").view_name == "api:users-me"
