# Generated by Django 4.2.2 on 2023-07-05 08:42

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
            field=models.UUIDField(default=uuid.UUID('bbd68b2a-6675-4814-b94c-78638b5d8e70')),
        ),
        migrations.AlterField(
            model_name='job',
            name='cancel_code',
            field=models.UUIDField(default=uuid.UUID('dbf178d3-56f1-4d11-9095-5080560dbfba')),
        ),
        migrations.AlterField(
            model_name='job',
            name='complete_code',
            field=models.UUIDField(default=uuid.UUID('91becfad-e5d8-4694-b5fc-d48986b9cd18')),
        ),
    ]
