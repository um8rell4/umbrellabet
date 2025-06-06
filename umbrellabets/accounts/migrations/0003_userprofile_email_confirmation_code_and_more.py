# Generated by Django 4.2.21 on 2025-05-28 22:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_confirmation_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, verbose_name='Код подтверждения email'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='Email подтвержден'),
        ),
    ]
