from django.urls import path
from . import views


app_name = 'listings'

urlpatterns = [
    path('',views.daftar_produk, name='daftar_produk'),
    path('<slug:kategori_slug>',views.daftar_produk,name='produk_berdasarkan_kategori'),
    path('<slug:kategori_slug>/<slug:produk_slug>/',views.detail_produk,name='detail_produk'),
]
