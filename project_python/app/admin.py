from django.contrib import admin
from .models import Usuario, Tarefa

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Campos a serem exibidos na listagem de usuários

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status', 'usuario')
    list_filter = ('status', 'usuario')  # Adiciona filtros no painel de administração