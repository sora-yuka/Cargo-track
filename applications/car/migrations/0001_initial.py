# Generated by Django 4.2.2 on 2023-07-04 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='CarDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.TextField()),
                ('documents_file', models.FileField(blank=True, null=True, upload_to='car/documents/')),
            ],
        ),
        migrations.CreateModel(
            name='CarEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_manufacture', models.PositiveIntegerField()),
                ('load_capacity', models.CharField(max_length=75)),
                ('car_image', models.ImageField(upload_to='car/images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_brand', to='car.carbrand')),
                ('car_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.cartype')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_documents', to='car.cardocument')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_equipment', to='car.carequipment')),
            ],
        ),
    ]
