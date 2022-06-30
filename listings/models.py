from django.db import models
from django.urls import reverse
import os
# Create your models here.
class Kategori(models.Model):
    """
    Kelas kategori
    ----------------------------


    membuat mmodel untuk kategori barang
    nama  = nama kategori
    slug = slug
    
    """
    nama = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        """
        ordering = mengurutkan basis data sesuai field nama
        verbose_name_plural = memberikan label pada nama model
        """
        ordering = ('-nama',)
        verbose_name_plural = 'kategori'

    def __str__(self):
        
        return self.nama
    
    def get_absolute_url(self):
        return reverse("listings:produk_berdasarkan_kategori", args=[self.slug])
    

class Produk(models.Model):
    """
    model produk
    -----------------

    kategori = kategori barang sesuai model basis data sebelumnya
    nama = nama produk
    slug = slug
    gambar = gambar produk
    deskripsi = deskripsi dari produk
    harga = harga barang
    ketersediaan = ada atau tidaknya barang
    """
    def lokasi_ganti_nama(instance,nama_file):
        upload_to = 'produk/'
        ext=nama_file.split('.')[-1]

        nama_file = '{}.{}'.format(instance.slug,ext)

        return os.path.join(upload_to,nama_file)

    kategori = models.ForeignKey(
        Kategori, related_name='produks',
        on_delete=models.CASCADE)
    nama = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    gambar = models.ImageField(upload_to=lokasi_ganti_nama)
    deskripsi =models.TextField()
    harga = models.DecimalField(max_digits=15, decimal_places=0)
    ketersediaan = models.BooleanField(default=True)

    class Meta:
        """
        mengurutkan tampilan sesuai field nama
        """
        ordering = ('-nama',)
        verbose_name_plural = 'Produk'
    
    def get_absolute_url(self):
        return reverse("listings:detail_produk", args=[self.kategori.slug, self.slug])
    