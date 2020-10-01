from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'categoria', 'imagen', 'texto_corto', 'detalle', 'precio','avalible')
        required= ('nombre', 'categoria', 'imagen', 'texto_corto', 'detalle', 'precio','avalible')

        widgets = {
	        'nombre':forms.TextInput(attrs={'class':'form-control'}),
	        'categoria':forms.Select(attrs={'class':'form-control'}),
	        'imagen':forms.FileInput(attrs={'class':'form-control-file'}),
	        'texto_corto':forms.Textarea(attrs={'class':'form-control'}),
	        'detalle':forms.Textarea(attrs={'class':'form-control'}),
	        'precio':forms.TextInput(attrs={'class':'form-control'})
        }