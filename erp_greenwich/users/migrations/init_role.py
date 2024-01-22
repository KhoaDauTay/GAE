# Generated by Django 3.2.10 on 2022-02-21 16:15
from django.db import migrations

from erp_greenwich.utils import Role as ROLE


def add_role(apps, schema_editor):
    Role = apps.get_model('users', 'Role')
    try:
        Role.objects.bulk_create([
            Role(
                name=ROLE.ADMIN.name
            ),
            Role(
                name=ROLE.STAFF.name
            ),
            Role(
                name=ROLE.STUDENT.name
            ),
            Role(
                name=ROLE.SECURITY.name
            ),
            Role(
                name=ROLE.MANAGER.name
            )
        ])
    except Exception as e:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_auto_20220226_1819'),
    ]

    operations = [migrations.RunPython(add_role, migrations.RunPython.noop)]
