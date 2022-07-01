import imp
from django import forms
from django.forms import NumberInput


class FormTambahProdukKeKeranjang(forms.Form):
    kuantitas = forms.IntegerField(
        min_value=1,
        widget=NumberInput(attrs={
            'class' :'form-control text-center px-3',
            'value': 1
        })
    )