# Generated by Django 4.2.2 on 2023-07-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydriverprofile',
            name='status',
            field=models.CharField(choices=[('free', 'free'), ('busy', 'busy')], default='free', max_length=55),
        ),
    ]
