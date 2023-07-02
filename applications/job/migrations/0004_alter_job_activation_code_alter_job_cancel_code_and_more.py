# Generated by Django 4.2.2 on 2023-07-01 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_activation_code_alter_job_cancel_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_code',
            field=models.UUIDField(default=uuid.UUID('cab96059-b146-4469-87c1-dd53e1b0ac35')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('f88c2c30-e280-43d8-afa7-8751601a596a')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('6a0ad51a-0b84-45a7-984d-1808b2e60cd3')),
        ),
    ]
