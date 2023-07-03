# Generated by Django 4.2.2 on 2023-07-03 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
        ('profiles', '0003_alter_driverprofile_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydriver',
            old_name='is_company_dirver',
            new_name='company_dirver',
        ),
        migrations.RenameField(
            model_name='driverprofile',
            old_name='is_driver',
            new_name='driver',
        ),
        migrations.RenameField(
            model_name='shipperprofile',
            old_name='is_shipper',
            new_name='shipper',
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='is_company_dirver',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='is_driver',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='is_shipper',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='companydriver',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_driver_car', to='car.carinfo'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='auto_park',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_autopark', to='car.carinfo'),
        ),
    ]
