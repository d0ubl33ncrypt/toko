from django.shortcuts import get_object_or_404, render, redirect
from .models import Kategori,Produk, Ulasan
from .forms import FormUlasan
from cart.forms import FormTambahProdukKeKeranjang

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
        request, 'produk/daftar.html',
        {
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

    if request.method == 'POST':
        form_ulasan = FormUlasan(request.POST)

        if form_ulasan.is_valid():
            cf = form_ulasan.cleaned_data

            nama_penulis ="Rahasia"
            Ulasan.objects.create(
                produk = produk,
                penulis = nama_penulis,
                rating = cf['rating'],
                teks = cf['teks']
            )

        return redirect(
            'listings:detail_produk',
            kategori_slug=kategori_slug,produk_slug=produk_slug)

    else:
        form_ulasan = FormUlasan()
        form_produk_keranjang = FormTambahProdukKeKeranjang()

        return render(request,'produk/detail.html',
        {
            'produk':produk,
            'form_ulasan': form_ulasan,
            'form_produk_keranjang':form_produk_keranjang
        })

