from rest_framework import serializers
from apps.ecommerce.models import Cliente, Vendedor, Produto, Compra


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"
        

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


class CompraClienteSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.ReadOnlyField(source="cliente.nome")
    class Meta:
        model = Compra
        fields = ['cliente_nome']

