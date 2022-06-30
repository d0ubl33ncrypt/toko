from django.test import TestCase
from ..models import Kategori,Produk

# Create your tests here.
# class KategoriModelTest(TestCase):
    
#     @classmethod
#     def setUpTestData(cls):
#         Kategori.objects.create(
#             nama='test1',slug='test1')

#     def test_kategori_nama(self):
#         kategori = Kategori.objects.get(id=1)
#         expected_object_name = f'{kategori.nama}'
#         self.assertEqual(expected_object_name,'test1')
    
#     def test_kategori_slug(self):
#         kategori = Kategori.objects.get(id=1)
#         expected_object_name = f'{kategori.slug}'
#         self.assertEqual(expected_object_name,'test1')  

class TestListingsModel(TestCase):
    def set_up_data(self):
        self.kategori  = Kategori.objects.create(
            nama = 'pengetesan_kategori1',slug='pengetesan_kategori1'
        )

    def test_kategori_model(self):
        self.assertEqual(self.kategori.nama,str(self.kategori))
