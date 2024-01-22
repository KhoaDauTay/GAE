from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ...core.views.base_view import BaseViewSet
from ..tasks import send_new_user_notification
from .serializers import (
    UserCreateSerializer,
    UserInviteSerializer,
    UserSerializer,
    UserUpdateSerializer,
)

User = get_user_model()


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializer
    lookup_field = "id"
    serializer_map = {
        "me": UserSerializer,
        "retrieve": UserSerializer,
        "create": UserCreateSerializer,
        "update": UserUpdateSerializer,
        "invite": UserInviteSerializer,
    }

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @staticmethod
    def notify_for_invite(obj: User, **kwargs):
        send_new_user_notification.delay(user_id=obj.id)

    @action(detail=False, methods=["POST"], url_name="invite", url_path="invite")
    def invite(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
