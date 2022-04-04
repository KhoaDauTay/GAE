import datetime
import logging

from django.conf import settings

from config import celery_app
from erp_greenwich.auth.models import LogRequest, LogUri

LOG = logging.getLogger(__name__)


@celery_app.task(
    max_retries=settings.CELERY_TASK_RETRIES,
    throws=(LogRequest.DoesNotExist,),
    name="Count request",
    resource_type="User",
    autoretry_for=(LogRequest.DoesNotExist,),
    retry_backoff=30,
)
def count_request(path: str):
    year = datetime.datetime.now().year
    mydate = datetime.datetime.now()
    month = str(mydate.strftime("%B")).lower()
    if path.startswith("/api/"):
        obj, created = LogUri.objects.get_or_create(uri=path)
        if created:
            obj = LogUri.objects.get(uri=path)
            if hasattr(obj, month):
                log_month = getattr(obj, month)
                log_month += 1
                setattr(obj, month, log_month)
                obj.save(update_fields=[f"{month}"])
            else:
                LOG.info("No month for count of uri")
        if hasattr(obj, month):
            log_month = getattr(obj, month)
            log_month += 1
            setattr(obj, month, log_month)
            obj.save(update_fields=[f"{month}"])
        else:
            LOG.info("No month for count of uri")

    log = LogRequest.objects.get(year=year)
    if hasattr(log, month):
        log_month = getattr(log, month)
        log_month += 1
        setattr(log, month, log_month)
        log.save(update_fields=[f"{month}"])
    else:
        LOG.info("No month for count")
