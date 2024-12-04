from django.db import models


class TahunAkademik(models.Model):
    # tahun
    tahun = models.IntegerField(null=True)
    # semester
    semester = models.IntegerField(null=True)
    pass


# Create your models here.
class MataKuliah(models.Model):
    # nama
    # kode
    # sks
    # semester
    pass


class Jadwal(models.Model):
    # dosen
    # mata_kuliah
    # hari 
    # jam_mulai
    # jam_selesai
    # semester
    # ruang
    # kuota_peserta
    # tahun_akademik
    pass


class KRS(models.Model):
    # tahun_akademik
    # mahasiswa
    # jadwal
    
    pass
