from django.db import models
from django.urls import reverse
import os
from django.core.validators import MinValueValidator, MaxValueValidator
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

    def buat_rerata_skor(self):
        rerata_skor = 0
        if self.ulasans.count() >0:
            total_skor = sum([ulasan.rating for ulasan in self.ulasans.all()])
            rerata_skor = total_skor/ self.ulasans.count()
        return round(rerata_skor,1)

    def get_absolute_url(self):
        return reverse("listings:detail_produk", args=[self.kategori.slug, self.slug])

    class Meta:
        """
        mengurutkan tampilan sesuai field nama
        """
        ordering = ('-nama',)
        verbose_name_plural = 'Produk'
    
   
    

    
class Ulasan(models.Model):
    """
    membuat model ulasan
    --------------------------
    produk = menghubungkan one to many antara produk dengan ulasan
    penulis = nama penulis
    rating = besaran penilaian 
    teks = isi ulasan
    dibuat = waktu dibuatnya ulasan
    
    """
    produk = models.ForeignKey(
        Produk,
        related_name='ulasans',
        on_delete=models.CASCADE
    )
    penulis = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    teks = models.TextField(blank=True)
    dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-dibuat',)

