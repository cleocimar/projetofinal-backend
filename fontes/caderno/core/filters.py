from django_filters import filterset
from core import models

class UsuarioFilter(filterset.FilterSet):
    nome = filterset.CharFilter(lookup_expr='icontains')
    perfil = filterset.ChoiceFilter(choices=models.Usuario.Perfil)
    apelido = filterset.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Usuario
        fields = ('nome', 'perfil', 'apelido', )

class AulaFilter(filterset.FilterSet):
    
    instituicao = filterset.CharFilter(lookup_expr='icontains')
    data_aula = filterset.CharFilter(lookup_expr='icontains')
    disciplina = filterset.CharFilter(lookup_expr='icontains')
    conteudo = filterset.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Aula
        fields = ('instituicao', 'disciplina', 'conteudo', 'data_aula', )

class ComentarioFilter(filterset.FilterSet):

    texto = filterset.CharFilter(lookup_expr='icontains')
    data_comentario = filterset.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Comentario
        fields = ('texto', )


