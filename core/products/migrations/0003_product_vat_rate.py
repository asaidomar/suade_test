# Generated by Django 3.0.4 on 2020-03-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200319_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vat_rate',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=4),
        ),
    ]