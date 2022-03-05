import datetime
from base64 import b85encode
from uuid import uuid4

import jwt  # pip install pyjwt
from django.conf import settings
from django.utils.timezone import now
from oauthlib.common import to_unicode

from erp_greenwich.users.models import Role


def rsa_token_generator(request):
    now = datetime.datetime.utcnow()
    role: Role = request.user.role.name
    claims = {
        "iss": "GAE",
        "sub": request.user.id,
        "role": role,
        "username": request.user.username,
        "exp": now + datetime.timedelta(seconds=request.expires_in),
    }
    try:
        claims.update(request.claims)
    except Exception as e:
        print(e)
    private_pem = settings.PRIVATE_KEY
    token = jwt.encode(claims, private_pem, "RS256")
    token = to_unicode(token, "UTF-8")

    return token


def jwt_token_generator(request=None, key=settings.SECRET_KEY, algorithm="HS256"):
    """Generate a JWT access token with jti and exp claims
    jti - The "jti" (JWT ID) claim provides a unique identifier for the JWT.)
    exp - The "exp" (expiration time) claim identifies the expiration time
    Uses HS256 to sign and django SECRET_KEY as key.
    The minimal payload results in a token length of ca 144 bytes with the
    HMAC.SHA-256 algorithm
    """
    seconds = request.expires_in if request else 36000
    exp = int(now().timestamp()) + seconds
    jti = b85encode(uuid4().bytes).decode()

    claims = {"jti": jti, "exp": exp}
    return jwt.encode(claims, key, algorithm)
