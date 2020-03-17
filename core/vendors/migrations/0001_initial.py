# Generated by Django 3.0.4 on 2020-03-17 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Vendor System Creation date')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Vendor update date')),
                ('name', models.CharField(max_length=255, verbose_name='Vendor Name')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Vendor Code')),
                ('country', models.CharField(max_length=255, verbose_name='Vendor Country')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10, verbose_name='Vendor Status')),
                ('address', models.CharField(max_length=255, verbose_name='Vendor Street Address')),
                ('city', models.CharField(max_length=255, verbose_name='Vendor City Address')),
                ('zip', models.CharField(max_length=255, verbose_name='Vendor Zip Code Address')),
                ('phone', models.CharField(max_length=255, verbose_name='Vendor Phone number')),
                ('vat_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vendor VAT Number')),
                ('iban', models.CharField(blank=True, max_length=30, null=True, verbose_name='Vendor IBAN number')),
            ],
        ),
        migrations.CreateModel(
            name='VendorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Vendor Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='VendorTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Vendor Category tag')),
            ],
        ),
        migrations.CreateModel(
            name='VendorReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('stars', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='members.Member')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='vendors.Vendor')),
            ],
        ),
        migrations.AddField(
            model_name='vendor',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='vendors', to='vendors.VendorCategory'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='vendors', to='vendors.VendorTag'),
        ),
    ]