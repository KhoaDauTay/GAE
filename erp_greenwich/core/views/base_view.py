from typing import Any, Optional

from django.db import transaction
from django.db.models import Manager
from django.db.models.base import ModelBase
from django.utils.translation import gettext_lazy as _
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from erp_greenwich.core.response import APIResponse


class BaseViewSet(ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = []
    required_scopes = ["music"]
    serializer_class = None
    filter_backends = [SearchFilter, OrderingFilter]
    filterset_fields = []
    ordering_fields = ["pk"]
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
        return self.model_manager.all().order_by("-id" "")

    def external_validate(self, **kwargs) -> bool:
        """
        Using for validation before using `is_valid` function for Serializer.
        Define function with format `external_validate_for_<action_name>` to execute validation beHttpResponsefore
        `is_valid` function call.
        It will return boolean and check HttpResponse with `is_valid` value. If all is true then call `save()` function
        :param kwargs:
        :return: bool
        """
        if hasattr(self, f"external_validate_for_{self.action}"):
            result = getattr(self, f"external_validate_for_{self.action}")(**kwargs)
            if isinstance(result, bool):
                return result
            else:
                return True if result else False
        else:
            return True

    def success_response(self, return_obj, message: str = ""):
        """
        Return the success response for API, serialize the return_obj with serializer_class for return data

        :param return_obj:
        :param message: Custom success message
        :return:
        """
        return APIResponse(
            status=status.HTTP_200_OK,
            success=True,
            messages=[
                _(f"{self.action_display} {self.model_display} successfully")
                if not message
                else message
            ],
            data=self.serializer_class(return_obj).data,
        )

    def failure_response(self, message: str = ""):
        """
        Return the failure response for API
        :param message: Custom failure message
        :return:
        """
        return APIResponse(
            status=status.HTTP_400_BAD_REQUEST,
            messages=[
                _(f"Cannot {self.action_display} {self.model_display}")
                if not message
                else message,
            ],
        )

    def notify(self, obj: Any, **kwargs):
        """
        Using to notify for create/update/action
        This function will execute after `.save()` function
        Define function with format `notify_for_<action_name>` to using notification function
        :param obj:
        :param kwargs:
        :return:
        """
        if hasattr(self, f"notify_for_{self.action}"):
            getattr(self, f"notify_for_{self.action}")(obj, **kwargs)

    def perform_create(self, serializer, **kwargs):
        """Just override `perform_create` function with **kwargs"""
        return serializer.save(**kwargs)

    def perform_update(self, serializer, **kwargs):
        """Just override `perform_update` function with **kwargs"""
        return serializer.save(**kwargs)

    def create(self, request, *args, **kwargs):
        """
        Create new object for model. Define Serializer and register at serializer_map
        format {"create": SomeThingSerializer}
        This function will run `.create` function on Serializer
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data: dict = request.data
        serializer: Serializer = self.get_serializer(data=data)
        external_check = self.external_validate()
        if serializer.is_valid(raise_exception=True) and external_check:
            with transaction.atomic():
                return_obj = self.perform_create(serializer)
            self.notify(return_obj, **kwargs)
            return self.success_response(return_obj)
        return self.failure_response()

    def update(self, request, *args, **kwargs):
        """
        Create new object for model. Define Serializer and register at serializer_map
        format {"update": SomeThingSerializer}
        This function will run `.update` function on Serializer

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data: dict = request.data
        obj: Any = self.get_object()
        serializer: Serializer = self.get_serializer(obj, data=data)
        self.external_validate(**kwargs)
        if serializer.is_valid(raise_exception=True):
            return_obj = self.perform_update(serializer)
            self.notify(return_obj, **kwargs)
            return self.success_response(return_obj)
        return self.failure_response()

    def create_nested_model(self, request, *args, **kwargs):
        """
        Create a related object with models. Implement this function and
        register {"action_name": SpecificSerializer} at serializer_map to use.
        This function will automatically execute `.create` function in SpecificSerializer

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data: dict = request.data
        serializer: Serializer = self.get_serializer(data=data)
        obj: Any = self.get_object()
        self.external_validate(**kwargs)
        if serializer.is_valid(raise_exception=True):
            return_obj = self.perform_create(serializer, obj=obj)
            self.notify(return_obj, **kwargs)
            return self.success_response(return_obj)
        return self.failure_response()
