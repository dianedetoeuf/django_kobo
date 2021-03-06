# Generated by Django 2.0.5 on 2018-05-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0004_auto_20180507_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ame',
            options={'verbose_name': 'AME', 'verbose_name_plural': 'AME'},
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='answergps',
            options={'verbose_name': 'GPS', 'verbose_name_plural': 'GPS'},
        ),
        migrations.AlterModelOptions(
            name='answergs',
            options={'verbose_name': 'Good or Service', 'verbose_name_plural': 'Goods and Services'},
        ),
        migrations.AlterModelOptions(
            name='answerhhmembers',
            options={'verbose_name': 'HH Members', 'verbose_name_plural': 'HH Members'},
        ),
        migrations.AlterModelOptions(
            name='answernr',
            options={'verbose_name': 'Natural Resource', 'verbose_name_plural': 'Natural Resources'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='survey_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
