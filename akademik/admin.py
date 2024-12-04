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
    pass

@admin.register(MataKuliah)
class MataKuliahAdmin(ModelAdmin):
    pass

@admin.register(Jadwal)
class JadwalAdmin(ModelAdmin):
    pass

@admin.register(KRS)
class KRSAdmin(ModelAdmin):
    pass