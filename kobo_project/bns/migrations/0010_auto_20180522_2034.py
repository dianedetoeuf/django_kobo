# Generated by Django 2.0.5 on 2018-05-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0009_auto_20180522_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answergps',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True),
        ),
        migrations.AlterField(
            model_name='answergps',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=29, null=True),
        ),
    ]