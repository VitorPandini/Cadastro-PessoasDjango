from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome_completo= models.CharField(max_length=255)
    data_nascimento= models.DateField(null=True)
    ativa=models.BooleanField(default=True)
    