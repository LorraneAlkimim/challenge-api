# Generated by Django 4.2.6 on 2023-11-08 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_commissionpercentagebyweekday_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['code', 'description']},
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['date', 'invoice_code']},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'ordering': ['seller_code', 'name']},
        ),
        migrations.AlterModelTable(
            name='commissionpercentagebyweekday',
            table='commission_percentage_by_weekday',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
        migrations.AlterModelTable(
            name='sale',
            table='sale',
        ),
        migrations.AlterModelTable(
            name='saleproduct',
            table='sale_product',
        ),
        migrations.AlterModelTable(
            name='seller',
            table='seller',
        ),
    ]
