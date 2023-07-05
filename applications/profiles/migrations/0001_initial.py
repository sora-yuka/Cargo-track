# Generated by Django 4.2.2 on 2023-07-04 14:48

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
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('billing_address', models.CharField(blank=True, max_length=155, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/images/')),
                ('shipper', models.BooleanField(blank=True, default=False)),
                ('driver', models.BooleanField(blank=True, default=False)),
                ('company_driver', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShipperProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
            ],
            bases=('profiles.baseprofile',),
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=155, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=30, null=True)),
                ('company_license', models.TextField(blank=True, null=True)),
                ('company_license_file', models.FileField(blank=True, null=True, upload_to='company license/license/<django.db.models.fields.CharField>/')),
                ('insurance_contract', models.TextField(blank=True, null=True)),
                ('insurance_contract_file', models.FileField(blank=True, null=True, upload_to='campany contract/contract/<django.db.models.fields.CharField>/')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('billing_address', models.CharField(blank=True, max_length=155, null=True)),
                ('mc_dot_number', models.CharField(blank=True, max_length=10, null=True)),
                ('company_user', models.BooleanField(blank=True, default=False)),
                ('auto_park', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_autopark', to='car.carinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
                ('bio', models.TextField(blank=True, null=True)),
                ('mc_dot_number', models.CharField(blank=True, max_length=10, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_car', to='car.carinfo')),
            ],
            bases=('profiles.baseprofile',),
        ),
        migrations.CreateModel(
            name='CompanyDriverProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.baseprofile')),
                ('bio', models.TextField(blank=True, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_driver_car', to='car.carinfo')),
            ],
            bases=('profiles.baseprofile',),
        ),
    ]
