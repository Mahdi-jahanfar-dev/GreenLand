# Generated by Django 5.2.1 on 2025-06-03 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_zone_latitude_zone_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('solidMoisture', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.zone')),
            ],
        ),
    ]
