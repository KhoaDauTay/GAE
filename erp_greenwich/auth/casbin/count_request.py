import logging

from ..tasks import count_request

LOG = logging.getLogger(__name__)


class CountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            LOG.info("Request by anonymous")
            response = self.get_response(request)
            return response
        path = request.path
        LOG.info("Request go to count")
        count_request.delay(path=path)
        LOG.info("Complete to count request")
        response = self.get_response(request)
        return response
