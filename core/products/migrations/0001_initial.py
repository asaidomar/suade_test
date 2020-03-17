# Generated by Django 3.0.4 on 2020-03-17 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Product creation date')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Product update date')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Product Code')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product Brand')),
                ('description', models.CharField(max_length=255, verbose_name='Product description')),
                ('price', models.PositiveIntegerField(verbose_name='Product price, excl. taxes')),
                ('currency', models.CharField(max_length=15, verbose_name='Product Currency')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendors.Vendor')),
            ],
        ),
    ]