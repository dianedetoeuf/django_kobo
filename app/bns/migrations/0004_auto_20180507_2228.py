# Generated by Django 2.0.5 on 2018-05-07 19:28

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0003_auto_20180507_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answergps',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
