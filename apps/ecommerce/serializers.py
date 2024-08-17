from rest_framework import serializers
from apps.ecommerce.models import Cliente, Vendedor, Produto, Compra
from apps.ecommerce.validators import cpf_invalido, cnpj_invalido, nome_invalido, celular_invalido


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"
    
    def validate(self, dados):
        if cnpj_invalido(dados['cnpj']):
            raise serializers.ValidationError({'cnpj':'O CNPJ precisa ser válido.'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras.'})
        
        return dados
    
        

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
    
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter um valor válido.'})
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras.'})
        if celular_invalido(dados['telefone']):
            raise serializers.ValidationError({'telefone':'O telefone precisa seguir o modelo: 86 99999-9999 (respeitando traços e espaços).'})
        
        return dados


class CompraClienteSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.ReadOnlyField(source="cliente.nome")
    class Meta:
        model = Compra
        fields = ['cliente_nome']

