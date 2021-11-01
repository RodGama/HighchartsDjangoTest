from django.db import models
import time

class Rate(models.Model):
    nome = models.CharField(max_length=30)
    cotacao = models.DecimalField(decimal_places=4, max_digits=10)
    data = models.DateField()

    #def __dict__(self, *args, **kwargs):
    #    modelo = {'timestamp' : self.data ,'cotacao' : f'{self.cotacao}'.replace(",",".")}
    #    return modelo