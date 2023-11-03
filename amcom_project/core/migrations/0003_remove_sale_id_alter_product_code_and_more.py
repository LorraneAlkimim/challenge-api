# Generated by Django 4.2.6 on 2023-11-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sale_saleproduct_sale_products_sale_seller_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='invoice_code',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_code',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CommissionPercentageByWeekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.PositiveIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('minimum_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('maximum_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'unique_together': {('weekday',)},
            },
        ),
    ]
