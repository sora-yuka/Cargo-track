# Generated by Django 4.2.2 on 2023-07-03 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pickup_location', models.CharField(max_length=200)),
                ('pickup_date', models.CharField(max_length=100)),
                ('delivery_date', models.CharField(max_length=100)),
                ('destination_location', models.CharField(max_length=200)),
                ('weight_of_goods', models.CharField(max_length=100)),
                ('type_of_goods', models.CharField(max_length=100)),
                ('required_equipment', models.CharField(max_length=200)),
                ('special_instruction', models.TextField(blank=True, null=True)),
                ('activation_code', models.UUIDField(default=uuid.UUID('aeb4a0ce-499d-45de-b55e-d20a53155e75'))),
                ('complete_code', models.UUIDField(default=uuid.UUID('6ce22aa2-a727-428e-9081-a04bb4208335'))),
                ('cancel_code', models.UUIDField(default=uuid.UUID('8a75b0e9-6f18-4574-814a-5dd89a5ac12c'))),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Looking for shipper', 'Looking for shipper'), ('Negotiations are underway', 'Negotiations are underway'), ('Delivering', 'Delivering'), ('Completed', 'Completed')], default='Looking for shipper', max_length=100)),
                ('is_confirm', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
