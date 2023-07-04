# Generated by Django 4.2.2 on 2023-07-03 08:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_activation_code_alter_job_cancel_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_code',
            field=models.UUIDField(default=uuid.UUID('c2c8836e-1116-47f1-a6ab-a6b23b8891f6')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('eca67fb0-9833-44ab-b4d0-1f24b8ad5520')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('7b721f04-1800-403c-8e23-88d6777bb07c')),
        ),
    ]
