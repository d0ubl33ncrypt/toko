from django.shortcuts import get_object_or_404, render
from .models import Kategori,Produk

# Create your views here.
def daftar_produk(request,kategori_slug=None):
    kategoris = Kategori.objects.all()
    


    if kategori_slug:
        '''
        membuat filter pilihan variabel yang diminta untuk ditampilkan
        '''
        kategori_diminta = get_object_or_404(Kategori, slug=kategori_slug)
        produks = Produk.objects.filter(kategori=kategori_diminta)

    else:
        kategori_diminta = None
        produks = Produk.objects.all()


    return render(
        request, 'produk/daftar.html',{
            'kategoris':kategoris,
            'kategori_diminta' : kategori_diminta,
            'produks': produks
        }
    )

def detail_produk(request,kategori_slug,produk_slug):
    kategori = get_object_or_404(Kategori, slug=kategori_slug)
    produk = get_object_or_404(
        Produk,
        kategori_id = kategori.id,
        slug=produk_slug
    )

    return render(request,'produk/detail.html',{
        'produk':produk
    })