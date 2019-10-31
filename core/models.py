from django.db import models


# Create your models here.
class Caixa(models.Model):
    numero = models.IntegerField("Número")
    etiqueta = models.CharField(max_length=50)
    cor = models.CharField(max_length=40)
    ordering = ("numero",)

    def __str__(self):
        return "%05.d - %s (%s)" % (self.numero, self.etiqueta, self.cor)


class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    nome_mae = models.CharField("Nome da mãe", max_length=100)
    telefone = models.CharField(max_length=16)
    GRUPO_AMIGO_CHOICES = [("prédio", "prédio"),
                           ("escola", "escola")
                           ]
    grupo_amigo = models.CharField("Grupo de amigo", choices=GRUPO_AMIGO_CHOICES, max_length=10)
    ordering = ("nome",)

    def __str__(self):
        return "%s %s" % (self.nome, self.telefone)

    class Meta:
        verbose_name = "Amigo"
        verbose_name_plural = "Amigos"


class Colecao(models.Model):
    nome = models.CharField(max_length=50)
    ordering = ("nome",)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "coleção"
        verbose_name_plural = "coleções"


class Revista(models.Model):
    numero_edicao = models.IntegerField("Número da edição")
    ano = models.IntegerField("Ano de publicação")
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)

    ordering = ("numero",)

    def __str__(self):
        return "n° %05.d - %s (%s)" % (self.numero_edicao, self.colecao, self.ano)


class Emprestimo(models.Model):
    data_emprestimo = models.DateField("Data do emprestimo")
    data_devolucao = models.DateField("Data da devolução")
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    amigo = models.ForeignKey(Amigo, on_delete=models.CASCADE)

    ordering = ("data_emprestimo",)

    def __str__(self):
        return "Empréstimo %s" % (self.data_emprestimo.strftime("%d/%m/%Y"))

    class Meta:
        verbose_name = "empréstimo"
        verbose_name_plural = "empréstimos"
