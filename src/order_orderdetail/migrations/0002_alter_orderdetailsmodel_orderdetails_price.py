# Generated by Django 4.2.4 on 2023-11-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_orderdetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailsmodel',
            name='OrderDetails_price',
            field=models.FloatField(),
        ),
    ]
