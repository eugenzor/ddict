# Generated by Django 2.0 on 2017-12-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddict', '0005_auto_20171225_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sound',
            name='friq',
        ),
        migrations.AddField(
            model_name='sound',
            name='freq',
            field=models.FloatField(null=True, verbose_name='Frequency'),
        ),
    ]