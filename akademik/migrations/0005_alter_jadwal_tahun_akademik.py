# Generated by Django 5.1.1 on 2024-12-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0004_jadwal_dosen_jadwal_hari_jadwal_jam_mulai_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='tahun_akademik',
            field=models.IntegerField(),
        ),
    ]