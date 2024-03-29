import pytest
from django.test import RequestFactory

from erp_greenwich.users.api.views import UserViewSet
from erp_greenwich.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "avatar": None,
            "client": {
                "about_me": "",
                "address": "",
                "city": "",
                "country": "",
                "postal_code": "",
            },
            "email": user.email,
            "first_name": "",
            "id": user.id,
            "last_name": "",
            "name": user.name,
            "role": "No role",
        }
