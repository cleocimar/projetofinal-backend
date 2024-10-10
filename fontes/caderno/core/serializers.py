from rest_framework import serializers
from core import models

class UsuarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class AulaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aula
        fields = '__all__'

class UsuarioAulaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsuarioAula
        fields = '__all__'

class ComentarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = '__all__'

class AnexoAulaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnexoAula
        fields = '__all__'

class AnexoComentarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnexoComentario
        fields = '__all__'
