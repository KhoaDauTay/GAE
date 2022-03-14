from casbin_adapter.models import CasbinRule
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create policy with read csv"

    def handle(self, *args, **kwargs):
        CasbinRule.objects.bulk_create(
            [
                CasbinRule(ptype="p", v0="admin", v1="*", v2="*"),
                CasbinRule(ptype="p", v0="users:list", v1="users:list", v2="GET"),
                CasbinRule(ptype="p", v0="users:me", v1="users:me", v2="GET"),
                CasbinRule(
                    ptype="p", v0="users:retrieve", v1="users:retrieve", v2="GET"
                ),
                # Applications
                CasbinRule(
                    ptype="p",
                    v0="applications:create",
                    v1="applications:create",
                    v2="POST",
                ),
                CasbinRule(
                    ptype="p", v0="applications:list", v1="applications:list", v2="GET"
                ),
                CasbinRule(
                    ptype="p",
                    v0="applications:retrieve",
                    v1="applications:retrieve",
                    v2="GET",
                ),
                CasbinRule(
                    ptype="p",
                    v0="applications:update",
                    v1="applications:update",
                    v2="PUT",
                ),
                CasbinRule(
                    ptype="p",
                    v0="applications:destroy",
                    v1="applications:destroy",
                    v2="DELETE",
                ),
                CasbinRule(ptype="g", v0="student", v1="users:list"),
                CasbinRule(ptype="g", v0="student", v1="users:me"),
                CasbinRule(ptype="g", v0="student", v1="users:retrieve"),
            ]
        )
        self.stdout.write(self.style.SUCCESS("Successfully create policy"))
