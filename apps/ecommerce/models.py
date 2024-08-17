from django.db import models
 

class Vendedor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True, default="")
    
    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    CATEGORIAS = {
        "ET": "Eletrônicos",
        "MO": "Móveis",
        "MD": "Moda",
        "AL": "Alimentos",
        "VS": "Vestuário",
        "OT": "Outros",
    }
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(max_length=700)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, default="OT")
    
    def __str__(self):
        return self.nome
    

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Compra de {self.cliente} - {self.data}"