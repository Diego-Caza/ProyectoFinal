from django import forms
from .models import Tienda
##from django.contrib.gis.db import forms
class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ('nombre_tienda', 'descripcion', 'imagen', 'ubicacion')
        requiered = ('nombre', 'descripcion', 'imagen', 'ubicacion')

        widgets = {

            'nombre_tienda':forms.TextInput(attrs={'class':'form-control'}),
	        'descripcion':forms.Textarea(attrs={'class':'form-control'}),
	        'imagen':forms.FileInput(attrs={'class':'form-control-file'}),
            'ubicacion':forms.TextInput(attrs={'class':'form-control'}),
	        #'ubicacion':forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
        }