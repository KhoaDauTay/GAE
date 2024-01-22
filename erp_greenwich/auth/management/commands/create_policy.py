from casbin_adapter.models import CasbinRule
from django.conf import settings
from django.core.management.base import BaseCommand

from erp_greenwich.utils.get_action import read_file_json


class Command(BaseCommand):
    help = "Create policy with read csv"

    def handle(self, *args, **kwargs):
        scopes_path = settings.SCOPES_JSON_PATH
        scopes: dict = read_file_json(scopes_path)
        keys = list(scopes.keys())
        obj, created = CasbinRule.objects.get_or_create(
            ptype="p",
            v0="admin",
            v1="*",
            v2="*",
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Admin rule created"))
        for key in keys:
            key_split = key.split(":")
            basename = key_split[0]
            action = key_split[1]
            CasbinRule.objects.get_or_create(
                ptype="p",
                v0=f"{key}",
                v1=f"{basename}",
                v2=f"{action}",
            )
        self.stdout.write(self.style.SUCCESS("Successfully create policy"))
