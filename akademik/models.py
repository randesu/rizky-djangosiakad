from django.db import models


class TahunAkademik(models.Model):
    # tahun
    tahun = models.IntegerField(null=True)
    # semester
    semester = models.IntegerField(null=True)
    def __str__(self):
        return str(self.semester)
    pass


# Create your models here.
class MataKuliah(models.Model):
    # nama
    nama = models.CharField(blank=False, max_length=100)
    
    # kode
    kode = models.IntegerField(blank=False)
    
    # sks
    sks = models.IntegerField(blank=False)

    # semester
    semester = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nama)
    pass


class Jadwal(models.Model):
    # dosen
    dosen = models.CharField(blank=False, max_length=100)

    # mata_kuliah
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)

    # hari 
    hari = models.CharField(blank=False)

    # jam_mulai
    jam_mulai = models.TimeField()

    # jam_selesai
    jam_selesai = models.TimeField() 

    # semester
    semester = models.IntegerField(blank=False)
    
    # kuota_peserta
    kuota_peserta = models.IntegerField(blank=False)

    # tahun_akademik
    tahun_akademik = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.tahun_akademik)

    pass


class KRS(models.Model):
    # tahun_akademik
    tahun_akademik = models.ForeignKey(Jadwal, on_delete=models.CASCADE)

    # mahasiswa
    mahasiswa = models.CharField(blank=False, max_length=100)

    # jadwal
    jadwal = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    
    pass
