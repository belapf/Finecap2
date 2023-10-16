from django.forms import ModelForm
from django import forms
from .models import Reserva, Stand


class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.TextInput(attrs={'class': 'form-control' }),
            'quitado': forms.TextInput(attrs={'class': 'form-control' }),
        }

class StandForm(ModelForm):
    valor = forms.CharField(widget=forms.TextInput(attrs={"class": "money","placeholder": "Valor do stand",})
)
    class Meta: 
        model = Stand
        fields = '__all__'
        widgets = {
            'localizacao' : forms.TextInput(attrs={'class': 'form-control' }),
            'valor': forms.TextInput(attrs={'class': 'form-control' }),
        }
    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return valor.replace(",", ".")