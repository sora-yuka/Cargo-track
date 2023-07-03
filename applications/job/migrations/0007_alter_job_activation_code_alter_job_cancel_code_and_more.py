# Generated by Django 4.2.2 on 2023-07-03 09:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_activation_code_alter_job_cancel_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_code',
            field=models.UUIDField(default=uuid.UUID('bc6b4eae-c180-4072-931b-6f7f04b227a0')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('db8052d3-720a-4fec-832e-33ed3342b80c')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('619ec1cf-7650-40c5-8269-94123edb904f')),
        ),
    ]