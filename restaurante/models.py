from django.db import models


class Prato(models.Model):
    TIPOS_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Prato Principal', 'Prato Principal'),
        ('Sobremesa', 'Sobremesa'),
        ('Bebida', 'Bebida'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_CHOICES)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
