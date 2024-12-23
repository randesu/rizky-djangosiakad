# Generated by Django 5.1.1 on 2024-12-04 12:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0003_matakuliah_kode_matakuliah_nama_matakuliah_semester_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwal',
            name='dosen',
            field=models.CharField(default='echi', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='hari',
            field=models.CharField(default='senin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='jam_mulai',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='jam_selesai',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='kuota_peserta',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='matakuliah',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='akademik.matakuliah'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jadwal',
            name='tahun_akademik',
            field=models.ForeignKey(default=2024, on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik'),
            preserve_default=False,
        ),
    ]
