# Generated by Django 2.0 on 2017-12-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddict', '0004_auto_20171225_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='freq',
            field=models.FloatField(null=True, verbose_name='Friquency'),
        ),
        migrations.AlterField(
            model_name='word',
            name='transcription',
            field=models.CharField(max_length=100, null=True, verbose_name='Transcription'),
        ),
    ]
