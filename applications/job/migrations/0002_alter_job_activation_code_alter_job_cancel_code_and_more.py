# Generated by Django 4.2.2 on 2023-07-05 05:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_code',
            field=models.UUIDField(default=uuid.UUID('e78e6e7a-3168-4a52-a4fe-ddb684052afe')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('88e1bfa3-7549-4604-85a8-288225bfa1eb')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('a54e43ff-e865-427a-958f-2c9af66c0722')),
        ),
    ]
