# Generated by Django 4.2.2 on 2023-07-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=75)),
                ('year_of_manufacture', models.PositiveIntegerField()),
                ('car_type', models.CharField(choices=[('Euro-Track', 'Euro-Track'), ('Container', 'Container'), ('Tank', 'Tank'), ('Refrigerator', 'Refrigerator')], max_length=55)),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('load_capacity', models.CharField(max_length=75)),
                ('equipment', models.TextField(blank=True, null=True)),
                ('documents', models.TextField()),
                ('documents_file', models.FileField(blank=True, null=True, upload_to='car/<django.db.models.fields.CharField>/document')),
                ('car_image', models.ImageField(upload_to='car/images/')),
            ],
        ),
    ]
