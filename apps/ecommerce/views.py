from apps.ecommerce.models import Cliente, Vendedor, Produto, Compra
from apps.ecommerce.serializers import ClienteSerializer, VendedorSerializer, CompraClienteSerializer, CompraSerializer, ProdutoSerializer
from rest_framework import viewsets, generics


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    

class CompraClienteList(generics.APIView):
    def get_queryset(self):
        queryset = Compra.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = CompraClienteSerializer
    
    