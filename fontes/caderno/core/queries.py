from core import models
def obter_usuario_por_nome(nome):
    queryset = models.Usuario.objects.filter(nome__icontains=nome)
    return queryset

