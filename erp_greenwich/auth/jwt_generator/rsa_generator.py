import datetime

from django.conf import settings
from oauthlib.common import to_unicode


def rsa_token_generator(request):
    import jwt

    now = datetime.datetime.utcnow()

    claims = {
        'sub': request.user.id,
        'scope': request.scope,
        'exp': now + datetime.timedelta(seconds=request.expires_in)
    }

    claims.update(request.claims)
    private_pem = settings.PRIVATE_KEY
    token = jwt.encode(claims, private_pem, 'RS256')
    token = to_unicode(token, "UTF-8")

    return token
