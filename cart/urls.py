from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.detail_keranjang, name='detail_keranjang'),
    path('tambah/<int:produk_id>/',views.tambahkan_ke_keranjang,name='tambahkan_ke_keranjang'),
    path('kurangi/<int:produk_id>/',views.kurangi_dari_keranjang, name='kurangi_dari_keranjang'),
]
