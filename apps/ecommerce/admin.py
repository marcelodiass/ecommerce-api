from django.contrib import admin
from apps.ecommerce.models import Cliente, Vendedor, Produto, Compra

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'telefone')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome', 'email', 'cpf')
    ordering = ('nome',)
    
admin.site.register(Cliente, ClienteAdmin)


class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cnpj')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome', 'email', 'cnpj')
    ordering = ('nome',)
    
admin.site.register(Vendedor, VendedorAdmin)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria','vendedor')
    list_display_links = ('id', 'nome', 'vendedor')
    list_per_page = 20
    search_fields = ('nome', 'preco', 'vendedor')
    ordering = ('nome',)
    
admin.site.register(Produto, ProdutoAdmin)
