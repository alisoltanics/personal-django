from django.db import migrations
from django.contrib.auth.models import User
from django.conf import settings


def create_super_user(apps, schema_editor):
    """
        Creates superuser first time of running migrate command
    """
    User.objects.create_user(
        username=settings.USERNAME,
        password=settings.PASSWORD,
        is_superuser=True,
        is_staff=True
    )


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(create_super_user),
    ]
