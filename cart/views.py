from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from listings.models import Produk
from .forms import FormTambahProdukKeKeranjang
from decimal import Decimal


# Create your views here.
def ambil_keranjang(request):
    keranjang = request.session.get(settings.CART_ID)
    if not keranjang:
        keranjang = request.session[settings.CART_ID]={}
    
    return keranjang

def tambahkan_ke_keranjang(request, produk_id):
    keranjang = ambil_keranjang(request)
    produk = get_object_or_404(Produk,id=produk_id)
    produk_id = str(produk_id)
    form = FormTambahProdukKeKeranjang(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        if produk_id not in keranjang:
            keranjang[produk_id] = {
                'kuantitas' : 0,
                'harga': str(produk.harga)
            }

        if request.POST.get('timpa_kuantitas'):
            keranjang[produk_id]['kuantitas'] = cd['kuantitas']

        else:
            keranjang[produk_id]['kuantitas'] += cd['kuantitas']
        
        request.session.modified = True

        return redirect('cart:detail_keranjang')


def detail_keranjang(request):
    keranjang = ambil_keranjang(request)
    produk_ids = keranjang.keys()
    produks = Produk.objects.filter(id__in=produk_ids)
    keranjang_sementara = keranjang.copy()

    for produk in produks:
        barang_di_keranjang = keranjang_sementara[str(produk.id)]
        barang_di_keranjang['produk'] = produk
        barang_di_keranjang['harga_total'] = (Decimal(
            barang_di_keranjang['harga'])*barang_di_keranjang['kuantitas'])
        barang_di_keranjang['form_perbaharui_kuantitas'] = FormTambahProdukKeKeranjang(
            initial={
                'kuantitas' : barang_di_keranjang['kuantitas']
            }
        )

    total_harga_keranjang = sum(Decimal(barang['harga']) * barang['kuantitas'] for barang in keranjang_sementara.values())
    
    return render(request,'detail.html',{
            'keranjang' :keranjang_sementara.values(),
            'total_harga_keranjang' : total_harga_keranjang
            })

def kurangi_dari_keranjang(request, produk_id):
    keranjang = ambil_keranjang(request)
    produk_id = str(produk_id)
    if produk_id in keranjang:
        del keranjang[produk_id]

        request.session.modified = True

        return redirect('cart:detail_keranjang')

def bersihkan_keranjang(request):
    del request.session[settings.CART_ID]
