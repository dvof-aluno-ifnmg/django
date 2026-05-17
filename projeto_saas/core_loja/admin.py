from django.contrib import admin
from .models import Empresa, Produto
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramo')
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'empresa')
    list_filter = ('empresa',)
@admin.register(Cliente)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("os campos dos clientes")
    