from typing import Optional

from django.db.models import Manager
from django.db.models.base import ModelBase
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):
    serializer_class = None
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = []
    ordering_fields = ["pk"]
    permission_classes = []
    serializer_map = {}

    @property
    def action_display(self) -> str:
        """Display action name"""
        return self.action.replace("_", " ")

    def get_serializer_class(self):
        """
        Get action's serializer base on `serializer_map`
        :return: Serializer
        """
        return self.serializer_map.get(self.action, self.serializer_class)

    # TODO: create get_serializer_context

    @property
    def viewset_model(self) -> ModelBase:
        return getattr(self.serializer_class, "Meta").model

    @property
    def model_display(self) -> str:
        """Display ViewSet's model name"""
        return self.viewset_model.__name__.lower()

    @property
    def model_manager(self) -> Optional[Manager]:
        """
        Get models managers
        :return: Manager"""
        return getattr(self.viewset_model, "objects", None)

    def get_queryset(self):
        """
        Get models queryset base on Manager
        :return: QuerySet[Model]
        """
        return self.model_manager.all().order_by("-id")
