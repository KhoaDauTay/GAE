from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ...core.views.base_view import BaseViewSet
from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializer
    lookup_field = "id"
    serializer_map = {
        "me": UserSerializer,
        "retrieve": UserSerializer,
        "create": UserCreateSerializer,
    }

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
