from typing import Optional

from django.db.models import Q

from erp_greenwich.users.models import Client, User


def get_client(user: User) -> Optional[Client]:
    if not user.is_authenticated:
        return None
    client = Client.objects.filter(Q(user=user)).first()
    return client
