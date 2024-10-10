from rest_framework import viewsets
from rest_framework.decorators import action
from core import models,serializers, queries

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioModelSerializer

    # método customizado
    @action(detail=False, methods=['GET'])
    def obter_por_nome(self, request, *args, **kwargs):
        nome = request.query_params.get('nome')
        self.queryset = queries.obter_usuario_por_nome(nome)
        return super().list(request, *args, **kwargs)
            
class AulaViewset(viewsets.ModelViewSet):
    queryset = models.Aula.objects.all()
    serializer_class = serializers.AulaModelSerializer

class UsuarioAulaViewset(viewsets.ModelViewSet):
    queryset = models.UsuarioAula.objects.all()
    serializer_class = serializers.UsuarioAulaModelSerializer

class ComentarioViewset(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentarioModelSerializer

class AnexoAulaViewset(viewsets.ModelViewSet):
    queryset = models.AnexoAula.objects.all()
    serializer_class = serializers.AnexoAulaModelSerializer

class AnexoComentarioViewset(viewsets.ModelViewSet):
    queryset = models.AnexoComentario.objects.all()
    serializer_class = serializers.AnexoComentarioModelSerializer


