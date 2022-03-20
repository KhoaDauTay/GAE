import logging

from django.conf import settings
from django.contrib.auth import get_user_model

from config import celery_app
from erp_greenwich.utils.send_mail import send_notification_to_user

LOG = logging.getLogger(__name__)
User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task(
    max_retries=settings.CELERY_TASK_RETRIES,
    throws=(User.DoesNotExist,),
    name="Notify user was invited",
    resource_type="User",
    autoretry_for=(User.DoesNotExist,),
    retry_backoff=30,
)
def send_new_user_notification(user_id):
    LOG.info(user_id)
    user: User = User.objects.get(id=user_id)
    LOG.info(user)
    subject = f"[GAE]: Invite {user.name} for using application"

    context = {
        "username": user.username,
        "email": user.email,
        "name": user.name,
        "link": "https://gae-gw/accounts/login/",
    }

    template = "account/invite_user.html"
    send_notification_to_user(subject, context, template)
