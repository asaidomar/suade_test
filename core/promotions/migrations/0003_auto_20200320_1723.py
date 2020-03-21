# Generated by Django 3.0.4 on 2020-03-20 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200320_1455'),
        ('promotions', '0002_auto_20200320_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpromotion',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='products.Product'),
        ),
    ]