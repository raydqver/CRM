# Generated by Django 5.1.2 on 2024-11-06 20:28

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ads",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Название")),
                (
                    "promotion_channel",
                    models.CharField(max_length=128, verbose_name="Канал продвижения"),
                ),
                (
                    "budget",
                    models.DecimalField(
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
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to="products.product",
                        verbose_name="Услуга",
                    ),
                ),
            ],
            options={
                "verbose_name": "Реклама",
                "verbose_name_plural": "Рекламы",
            },
        ),
    ]
