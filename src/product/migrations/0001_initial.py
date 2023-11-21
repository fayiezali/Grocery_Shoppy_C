# Generated by Django 4.2.2 on 2023-08-28 19:08

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(blank=True, decimal_places=4, default=Decimal('0.00'), max_digits=10, null=True, verbose_name='Price')),
                ('product_image', models.ImageField(upload_to='Productes_File_Photo/%Y/%m/%d/')),
                ('product_is_active', models.BooleanField(default=False)),
                ('product_publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-product_publish_date',),
            },
        ),
    ]
