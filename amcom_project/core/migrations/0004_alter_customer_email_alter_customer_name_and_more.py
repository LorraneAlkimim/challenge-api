# Generated by Django 4.2.6 on 2023-11-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_sale_id_alter_product_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="seller",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="seller",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
