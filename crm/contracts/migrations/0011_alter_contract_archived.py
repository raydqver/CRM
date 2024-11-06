# Generated by Django 5.1.2 on 2024-11-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0010_alter_contract_archived"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="archived",
            field=models.BooleanField(
                choices=[(True, "Недействителен"), (False, "Действителен")],
                default=False,
                verbose_name="Срок действия",
            ),
        ),
    ]
