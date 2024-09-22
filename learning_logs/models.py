from django.db import models
from django.contrib.auth.models import User #Modelo de usuario prédefinido pelo django

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #O onwer será a variavel que contem o usuário que criou o topico
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Retorna uma representação em string do objeto."""
        return self.text

class Entry(models.Model): # Entra com algum dado
    """Informa sobre um topico em particular"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #Relaciona a entrada com o Banco de dados e deleta todas as entradas relacionadas com o topico
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: #Quando o django utilizar o model, ele vai criar um nome para o plural
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna uma representa o em string do objeto."""
        return self.text[:50] + "..."
