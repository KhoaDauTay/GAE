import json

from django.conf import settings
from django.core.management.base import BaseCommand

from erp_greenwich.utils.get_action import get_api_actions


class Command(BaseCommand):
    help = "Group permission with Label"

    def handle(self, *args, **kwargs):
        data = []
        scopes = get_api_actions().get("scopes")
        labels = get_api_actions().get("labels")
        print(labels)
        for label in labels:
            data.append({"label": label, "children": []})
        for child in data:
            for scope in scopes:
                """
                Create description of scope
                """
                name_scope = scope.split(":")
                basename: str = name_scope[0].replace(
                    "_", " "
                )  # name of scope: applications
                action_name: str = name_scope[1].replace(
                    "_", " "
                )  # name of action: create
                description = f"{action_name.title()} {basename.title()}"
                if child.get("label") == basename.title():
                    children: list = child.get("children")
                    children.append({"scope": scope, "description": description})
        json_path = settings.GROUP_SCOPES_JSON_PATH
        with open(json_path, "w+", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)

        self.stdout.write(self.style.SUCCESS("Successfully create permissions"))
