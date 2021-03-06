# Generated by Django 3.1.4 on 2021-01-01 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCarts',
            fields=[
                ('uc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('ad_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ad_country', models.CharField(max_length=50)),
                ('ad_state', models.CharField(max_length=50)),
                ('ad_city', models.CharField(max_length=50)),
                ('ad_full_address', models.CharField(max_length=100)),
                ('ad_pin', models.IntegerField()),
                ('ad_ph_number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('o_quantity', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.useraddresses')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
