from uuid import uuid4
from base64 import b85encode
import jwt  # pip install pyjwt
from django.conf import settings
from django.utils.timezone import now


def jwt_token_generator(
    request=None,
    key=settings.SECRET_KEY,
    algorithm='HS256'
):
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
