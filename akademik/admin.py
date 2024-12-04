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
class ProdiAdmin(ModelAdmin):
    pass

@admin.register(MataKuliah)
class ProdiAdmin(ModelAdmin):
    pass

@admin.register(Jadwal)
class ProdiAdmin(ModelAdmin):
    pass

@admin.register(KRS)
class ProdiAdmin(ModelAdmin):
    pass