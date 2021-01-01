# Generated by Django 3.1.4 on 2021-01-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarManufacturers',
            fields=[
                ('cm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cm_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarSeries',
            fields=[
                ('cs_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cs_name', models.CharField(max_length=50)),
                ('car_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.carmanufacturers')),
            ],
        ),
        migrations.CreateModel(
            name='PartsCategories',
            fields=[
                ('pc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pc_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('i_id', models.IntegerField(primary_key=True, serialize=False)),
                ('i_name', models.CharField(max_length=50)),
                ('car_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.carseries')),
                ('parts_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.partscategories')),
            ],
        ),
    ]
