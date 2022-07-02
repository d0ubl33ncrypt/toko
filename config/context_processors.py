from cart.views import ambil_keranjang
from decimal import Decimal

def keranjang(request):
    keranjang= ambil_keranjang(request)
    total_harga_keranjang = sum(Decimal(barang['harga']) * barang['kuantitas'] for barang in keranjang.values())

    return {
        'total_harga_keranjang' : total_harga_keranjang
    }