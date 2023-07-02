# Generated by Django 4.2.2 on 2023-07-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_recovery_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mc_dot_number',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
