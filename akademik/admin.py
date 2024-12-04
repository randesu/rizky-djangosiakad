from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    TahunAkademik,
    MataKuliah,
    Jadwal,
    KRS,
)
# Register your models here.

@admin.register(TahunAkademik)
class TahunAkademikAdmin(ModelAdmin):
    list_display = ['tahun', 'semester']
    pass

@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    list_display = ['nama', 'kode', 'sks','semester']

    pass

@admin.register(Jadwal)
class JadwalAdmin(ModelAdmin):
    list_display = ['dosen', 'matakuliah', 'hari','jam_mulai', 'jam_selesai',
                    'semester', 'kuota_peserta', 'tahun_akademik']

    pass

@admin.register(KRS)
class KRSAdmin(ModelAdmin):
    list_display = ['tahun_akademik', 'mahasiswa', 'jadwal']

    pass