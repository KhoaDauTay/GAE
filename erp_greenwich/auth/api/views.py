from erp_greenwich.auth.api.serializers import ApplicationSerializer
from erp_greenwich.core.views.base_view import BaseViewSet


class ApplicationViewSet(BaseViewSet):
    serializer_class = ApplicationSerializer
