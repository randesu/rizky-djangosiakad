# Generated by Django 5.1.1 on 2024-12-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tahunakademik',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tahunakademik',
            name='tahun',
            field=models.IntegerField(null=True),
        ),
    ]
