import json

from django.conf import settings
from django.core.management.base import BaseCommand

from erp_greenwich.utils.get_action import get_api_actions


class Command(BaseCommand):
    help = "Create permissions with url pattern"

    def handle(self, *args, **kwargs):
        data = {}
        for scope in get_api_actions():
            """
            Create description of scope
            """
            name_scope = scope.split(":")
            basename = name_scope[0].replace("_", " ")  # name of scope: album
            action_name = name_scope[1].replace("_", " ")  # name of action: create
            description = f"{action_name.title()} object of {basename.title()}"

            data.update({scope: description})
        json_path = settings.SCOPES_JSON_PATH
        with open(json_path, "w+", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)

        self.stdout.write(self.style.SUCCESS("Successfully create permissions"))
