# Generated by Django 4.2.6 on 2023-11-28 03:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CommissionPercentageByWeekday",
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
                (
                    "weekday",
                    models.PositiveIntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        unique=True,
                    ),
                ),
                (
                    "minimum_percentage",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                (
                    "maximum_percentage",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
            ],
            options={
                "db_table": "commission_percentage_by_weekday",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("name", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "db_table": "customer",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("code", models.CharField(max_length=50, unique=True)),
                ("description", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "commission_percentage",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
            ],
            options={
                "db_table": "product",
                "ordering": ["code", "description"],
            },
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "invoice_code",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="core.customer"
                    ),
                ),
            ],
            options={
                "db_table": "sale",
                "ordering": ["-date", "invoice_code"],
            },
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                ("name", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                (
                    "seller_code",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "seller",
                "ordering": ["seller_code", "name"],
            },
        ),
        migrations.CreateModel(
            name="SaleProduct",
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
                ("quantity", models.IntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.product"
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.sale"
                    ),
                ),
            ],
            options={
                "db_table": "sale_product",
            },
        ),
        migrations.AddField(
            model_name="sale",
            name="products",
            field=models.ManyToManyField(through="core.SaleProduct", to="core.product"),
        ),
        migrations.AddField(
            model_name="sale",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="core.seller"
            ),
        ),
        migrations.AddConstraint(
            model_name="saleproduct",
            constraint=models.UniqueConstraint(
                fields=("product", "sale"), name="once_per_sale_product"
            ),
        ),
    ]
