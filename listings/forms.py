from django import forms 
from .models import Ulasan

PILIHAN_ULASAN = [
    ('1','1'),('2','2'),
    ('3','3'),('4','4'),('5','5')]

class FormUlasan(forms.ModelForm):

    class Meta:
        model = Ulasan
        fields = ['teks','rating']
        widgets = {
            'teks':forms.Textarea(
                attrs={
                    'class':'form-control shadow px-2',
                    'rows':6
                }
            ),
            'rating':forms.RadioSelect
        }