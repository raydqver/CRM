# Generated by Django 5.1.2 on 2024-11-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0007_alter_contract_archived"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contract",
            name="archived",
        ),
    ]
