from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Especie(models.Model):
    nome = models.CharField(max_length = 100)
    imagem = models.ImageField()
    peso = models.DecimalField(max_digits=50, decimal_places = 2)
    altura = models.DecimalField(max_digits=50, decimal_places = 2)
    descricao = models.CharField(max_length = 100)
    categoria = models.ManyToManyField('Category', related_name= 'bispo')
        
        
    def __str__(self) :
        return self.nome
