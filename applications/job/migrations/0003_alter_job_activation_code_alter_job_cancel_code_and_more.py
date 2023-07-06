# Generated by Django 4.2.2 on 2023-07-06 06:32

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
            field=models.UUIDField(default=uuid.UUID('646fe8fe-7990-40de-9886-b7242cf6ef16')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('cff6f1f8-b3ea-4a8a-a0a9-27f1a12476e9')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('f3e7a3ab-add8-4cb6-a886-ca2cfe102df7')),
        ),
    ]