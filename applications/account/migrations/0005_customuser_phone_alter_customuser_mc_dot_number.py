# Generated by Django 4.2.2 on 2023-06-30 04:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_recovery_password_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=1, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mc_dot_number',
            field=models.CharField(max_length=10),
        ),
    ]
