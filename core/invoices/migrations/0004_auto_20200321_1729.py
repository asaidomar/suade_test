# Generated by Django 3.0.4 on 2020-03-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20200320_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='created_at',
            field=models.DateField(default='2020-03-21'),
        ),
    ]