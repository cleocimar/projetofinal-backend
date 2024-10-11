from rest_framework import serializers

class UsuarioObterPorNomeSerializersParams(serializers.Serializer):
    nome = serializers.CharField(required=True)

    