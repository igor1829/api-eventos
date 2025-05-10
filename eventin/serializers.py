from rest_framework import serializers
from .models import Evento, Participante, Inscricao
from .validator import nome_invalido, email_invalido, telefone_invalido, cpf_invalido

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ["id", "titulo", "descricao", "local", "data_evento", "capacidade"]

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ["id", "nome", "cpf", "email", "telefone"]
        
    def validate(self, dados):
        if nome_invalido(dados.get("nome", "")):
            raise serializers.ValidationError({"nome": "O nome deve ter pelo menos 3 caracteres e conter apenas letras"})
        if email_invalido(dados.get("email", "")):
            raise serializers.ValidationError({"email": "O e-mail deve ser válido"})
        if telefone_invalido(dados.get("telefone", "")):
            raise serializers.ValidationError({"telefone": "Número de telefone inválido"})
        if cpf_invalido(dados.get("cpf", "")):
            raise serializers.ValidationError({"cpf": "Número de CPF é inválido"})
        return dados

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ["id", "evento", "participante", "data_inscricao"]

class ListaInscricoesParticipantesSerializer(serializers.ModelSerializer):
    evento = serializers.ReadOnlyField(source="evento.titulo")
    class Meta:
        model = Inscricao
        fields = ["evento", "data_inscricao"]
        
class ListaInscricoesEventoSerializer(serializers.ModelSerializer):
    participante = serializers.ReadOnlyField(source="participante.nome")
    class Meta:
        model = Inscricao
        fields = ["participante", "data_inscricao"]

class ParticipanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ["id", "nome", "email", "telefone"]