from django.contrib import admin
from .models import Kategori, Produk
# Register your models here.

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    """
    memberikan apa saja yang perlu ditampilkan pada menu admin
    membuat slug otomatis terisi
    """
    list_display = ('nama','slug')
    prepopulated_fields = {'slug':('nama',)}

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = (
        'nama','kategori','slug',
        'harga','ketersediaan')
    list_filter = ('kategori','ketersediaan')
    list_editable = ('harga','ketersediaan')
    prepopulated_fields = {'slug':('nama',)}
    

