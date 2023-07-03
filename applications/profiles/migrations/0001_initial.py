# Generated by Django 4.2.2 on 2023-07-03 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=155, null=True)),
                ('last_name', models.CharField(blank=True, max_length=155, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('billing_address', models.CharField(blank=True, max_length=155, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShipperProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
                ('is_shipper', models.BooleanField(blank=True, default=True)),
            ],
            bases=('profiles.baseprofile',),
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=155, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=30, null=True)),
                ('company_license', models.TextField(blank=True, null=True)),
                ('company_license_file', models.FileField(blank=True, null=True, upload_to='company license/license/<django.db.models.fields.CharField>/')),
                ('insurance_contract', models.TextField(blank=True, null=True)),
                ('insurance_contract_file', models.FileField(blank=True, null=True, upload_to='campany contract/contract/<django.db.models.fields.CharField>/')),
                ('billing_address', models.CharField(blank=True, max_length=155, null=True)),
                ('mc_dot_number', models.CharField(blank=True, max_length=10, null=True)),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_autopark', to='car.carinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
                ('mc_dot_number', models.CharField(blank=True, max_length=10, null=True)),
                ('is_driver', models.BooleanField(blank=True, default=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_car', to='car.carinfo')),
            ],
            bases=('profiles.baseprofile',),
        ),
        migrations.CreateModel(
            name='CompanyDriver',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
                ('is_company_dirver', models.BooleanField(blank=True, default=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_driver_car', to='car.carinfo')),
            ],
            bases=('profiles.baseprofile',),
        ),
    ]
