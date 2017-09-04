from models import Mesa, Resultado
from django.forms.models import ModelForm

class NuevaMesa(ModelForm):
    class Meta:
        model = Mesa
        fields = ('nombre',)

class AddResultado(ModelForm):
    class Meta:
        model = Resultado
        fields = ('partido', 'votos')