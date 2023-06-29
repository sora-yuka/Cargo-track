# Generated by Django 4.2.2 on 2023-06-29 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recovery_code', models.CharField(max_length=55)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_recovery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]