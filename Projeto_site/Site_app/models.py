from django.db import models

class Pessoa(models.Model):
    #Lista de atributos com os tipos que deverão ser armazenados no banco de dados
    nomePessoa= models.CharField(max_length=100)
    sobrenomePessoa= models.CharField(max_length=100)
    telefonePessoa= models.CharField(max_length=20)
    estadoPessoa = models.CharField(max_length=2)  


    #Método da Classe:

    def registrarPessoa(self):
        self.save ()
        

        