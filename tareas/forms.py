from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = "date"


class ListaForm(forms.ModelForm):
    titulo_lista = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = models.Lista
        fields = ['titulo_lista']

