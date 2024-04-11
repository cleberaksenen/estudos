from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True) #Vai criar o número sequencial
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()



    

