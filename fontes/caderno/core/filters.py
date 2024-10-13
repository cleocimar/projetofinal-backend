from django_filters import filterset
from core import models

class UsuarioFilter(filterset.FilterSet):
    nome = filterset.CharFilter(lookup_expr='icontains')
    tipo = filterset.ChoiceFilter(choices=models.Usuario.Perfil)
    apelido = filterset.CharFilter(lookup_expr='icontains')
    apelido = filterset.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Usuario
        fields = ('nome', 'perfil', 'apelido', )

