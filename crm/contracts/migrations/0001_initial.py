# Generated by Django 5.1.2 on 2024-11-05 12:09

import contracts.models
import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                    "start_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата заключения"
                    ),
                ),
                ("end_date", models.DateTimeField(verbose_name="Период действия")),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(
                                Decimal("0"), message="Минимальное значение - 0"
                            )
                        ],
                        verbose_name="Сумма",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        null=True,
                        upload_to=contracts.models.contract_path,
                        verbose_name="Документ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="products.product",
                        verbose_name="Услуга",
                    ),
                ),
            ],
        ),
    ]