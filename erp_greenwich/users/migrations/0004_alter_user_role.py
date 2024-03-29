# Generated by Django 3.2.10 on 2022-02-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('STAFF', 'Staff'), ('SECURITY', 'Security'), ('STUDENT', 'Student'), ('MANAGER', 'Manager')], max_length=20, null=True),
        ),
    ]
