# Generated by Django 2.0.5 on 2018-06-24 18:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0031_nr_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='NRCollectPerDistrict',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nr', models.TextField(blank=True, null=True)),
                ('dataset_year', models.IntegerField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('landscape', models.TextField(blank=True, null=True)),
                ('avg_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('perc_hh_collect', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('stddev_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bns_nr_collect_district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NRCollectPerLandscape',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nr', models.TextField(blank=True, null=True)),
                ('dataset_year', models.IntegerField(blank=True, null=True)),
                ('landscape', models.TextField(blank=True, null=True)),
                ('avg_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('perc_hh_collect', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('stddev_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bns_nr_collect_landscape',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NRCollectPerVillage',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nr', models.TextField(blank=True, null=True)),
                ('dataset_year', models.IntegerField(blank=True, null=True)),
                ('village', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('landscape', models.TextField(blank=True, null=True)),
                ('avg_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('perc_hh_collect', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('stddev_collect_week', models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bns_nr_collect_village',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_id',
            field=models.UUIDField(default=uuid.UUID('3b74a7c6-c5b4-4d22-a04c-d51492f16dfa'), editable=False, primary_key=True, serialize=False),
        ),
    ]
