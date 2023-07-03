# Generated by Django 4.2.2 on 2023-07-03 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_job_activation_code_alter_job_cancel_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_code',
            field=models.UUIDField(default=uuid.UUID('61fbdb65-476b-463f-abbf-3fe25c9d4e7f')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('022251f2-b25e-4b8c-aff0-38430335a818')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('58d63555-d7c3-4ec9-9c77-a139a417dbb1')),
        ),
    ]
