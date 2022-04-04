from ..tasks import count_request


class CountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            response = self.get_response(request)
            return response
        response = self.get_response(request)
        path = request.path
        count_request.delay(path=path)
        return response
