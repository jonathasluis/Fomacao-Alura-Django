from datetime import datetime
from django.db import models

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'NEBULOSA'),
        ('ESTRELA', 'ESTRELA'),
        ('GALÁXIA', 'GALÁXIA'),
        ('PLANETA', 'PLANETA'),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False )
    legenda =models.CharField(max_length=150, null=False, blank=False )
    categoria = models.CharField(max_length=100, null=False, choices=OPCOES_CATEGORIA, default='' )
    descricao = models.TextField( null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicado = models.BooleanField(default=False)
    data_fotofrafia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"