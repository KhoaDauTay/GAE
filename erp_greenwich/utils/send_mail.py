import logging

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

LOG = logging.getLogger(__name__)


def send_notification_to_user(subject, context, template):
    """

    :param subject:
    :param context:
    :param template:
    :return:
    """
    message = ""
    html_message = render_to_string(template, context)
    user_email = context.get("email", None)

    # try:
    to_mails = [user_email]
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        to_mails,
        fail_silently=False,
        html_message=html_message,
    )
    # except Exception:
    #     LOG.warning("Can not send email to user")
