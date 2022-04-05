from rest_framework_simplejwt import authentication


class JwtAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = authentication.JWTAuthentication().authenticate(request)[0]
        response = self.get_response(request)
        return response
