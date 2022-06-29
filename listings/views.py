from django.shortcuts import render
from .models import Kategori,Produk

# Create your views here.
def daftar_produk(request):
    kategoris = Kategori.objects.all()
    produks = Produk.objects.all()

    return render(
        request, 'produk/daftar.html',{
            'kategoris':kategoris,
            'produks': produks
        }
    )