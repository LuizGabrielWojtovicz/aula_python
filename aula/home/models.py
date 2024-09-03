from django.db import models

class Aniversario(models.Model):
    nome = models.CharField("Nome", max_length=200)
    data = models.DateTimeField("Data")