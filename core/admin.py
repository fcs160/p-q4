from django.contrib import admin
from .models import *


# Register your models here
class AmigoAdmin(admin.ModelAdmin):
    list_display = ("nome", "nome_mae", "telefone", "grupo_amigo")
    search_fields = ("nome", "nome_mae")
    list_filter = ("grupo_amigo",)


class ColecaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


class CaixaAdmin(admin.ModelAdmin):
    list_display = ("numero", "etiqueta", "cor")
    list_filter = ("etiqueta", "cor")
    search_fields = ("etiqueta",)


class RevistaAdmin(admin.ModelAdmin):
    list_display = ("numero_edicao", "ano", "colecao")
    list_filter = ("ano", "colecao")


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("data_emprestimo", "data_devolucao")
    list_filter = ("data_emprestimo", "data_devolucao")
    date_hierarchy = "data_emprestimo"


admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Caixa, CaixaAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.site_header = "Painel de controle"
admin.site.index_title = "Recursos"
admin.site.site_title = "Gibiteca"
