from django import forms
from datetime import date
from .models import Compra

class FamiliarForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    edad = forms.IntegerField(label='Edad')
    parentesco = forms.CharField(max_length=50, label='Parentesco')
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, date.today().year)),label='Fecha de Nacimiento')

#class CompraForm(forms.Form):
#    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
#    precio = forms.FloatField(label='Precio')
#    cantidad = forms.IntegerField(label='Cantidad')

class VueloForm(forms.Form):
    origen = forms.CharField(widget=forms.Textarea, label='Origen')
    destino = forms.CharField(widget=forms.Textarea, label='Destino')
    fecha_salida = forms.DateField(widget=forms.SelectDateWidget, label='Fecha de Salida')
    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Horario')
    precio = forms.FloatField(label='Precio')

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['descripcion', 'precio', 'cantidad']