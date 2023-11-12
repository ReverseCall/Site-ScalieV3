# models.py
from django.db import models

class Mensagem(models.Model):
    conteudo = models.TextField()
    horario_envio = models.TimeField()
    dia_envio = models.DateField()
    ultima = models.BooleanField(default=False)
    mensagem_adicional = models.TextField(blank=True, null=True)
    audio_url = models.FileField(upload_to='audios/', null=True, blank=True)

    def __str__(self):
        return self.conteudo
