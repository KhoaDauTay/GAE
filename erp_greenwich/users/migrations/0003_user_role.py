# Generated by Django 3.2.10 on 2022-02-21 16:03

from django.db import migrations, models
import erp_greenwich.utils.enum


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220221_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[(erp_greenwich.utils.enum.Role['ADMIN'], 'Admin'), (erp_greenwich.utils.enum.Role['STAFF'], 'Staff'), (erp_greenwich.utils.enum.Role['SECURITY'], 'Security'), (erp_greenwich.utils.enum.Role['STUDENT'], 'Student'), (erp_greenwich.utils.enum.Role['MANAGER'], 'Manager')], max_length=5, null=True),
        ),
    ]