# Generated by Django 5.1.2 on 2024-11-05 12:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name="contract",
            name="end_date",
            field=models.DateTimeField(verbose_name="Действует до"),
        ),
    ]