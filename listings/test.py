from django.test import TestCase
from .models import Kategori,Produk

# Create your tests here.
class KategoriModelTest(TestCase):
    
    @classmethod
    def setUp(self):
        self.kategori1 = Kategori.objects.create(
            nama='test 1', slug='test-1'
        )
    
    def test_kategori_nama_dan_slug(self):
        self.assertEqual(self.kategori1.nama,'test 1')
        self.assertEqual(self.kategori1.slug,'test-1')