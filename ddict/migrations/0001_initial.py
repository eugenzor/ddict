# Generated by Django 2.0 on 2017-12-25 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.CharField(max_length=5, verbose_name='Sign')),
                ('friq', models.FloatField(verbose_name='Friquency')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='Name')),
                ('transcription', models.CharField(max_length=100, verbose_name='Transcription')),
                ('friq', models.FloatField(verbose_name='Friquency')),
                ('sounds', models.ManyToManyField(to='ddict.Sound')),
            ],
        ),
        migrations.AddField(
            model_name='phrase',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddict.Word'),
        ),
    ]
