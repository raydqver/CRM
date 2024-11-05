# Generated by Django 5.1.2 on 2024-11-05 11:02

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ads",
            name="budget",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[
                    django.core.validators.MinValueValidator(
                        Decimal("0"), message="Минимальное значение - 0"
                    )
                ],
                verbose_name="Бюджет",
            ),
        ),
    ]