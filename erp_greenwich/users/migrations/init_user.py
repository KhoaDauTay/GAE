# Generated by Django 3.2.10 on 2022-02-21 16:15
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations



def add_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    try:
        admin_user, created = User.objects.get_or_create(
            username='admin',
            email='admin@gmail.com',
            password=make_password('khoa0305'),
            name='admin',
            is_superuser=True,
        )
        User.objects.bulk_create([
            User(username='student',
                 email='student@gmail.com',
                 password=make_password('khoa0305'),
                 name='student',
                 ),
            User(username='staff',
                 email='staff@gmail.com',
                 password=make_password('khoa0305'),
                 name='staff',
                 ),
            User(username='security',
                 email='security@gmail.com',
                 password=make_password('khoa0305'),
                 name='security',
                 ),
            User(username='manager',
                 email='manager@gmail.com',
                 password=make_password('khoa0305'),
                 name='manager',
                 ),
        ])
    except Exception as e:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('users', 'init_role'),
    ]

    operations = [migrations.RunPython(add_user, migrations.RunPython.noop)]
