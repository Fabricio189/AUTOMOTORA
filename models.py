from django.db import models


# Create your models here.

class Marca(models.Model):
    #django agrega un id a todos los modelos(autoincrementable)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.Nombre, self.Descripcion)
    

class Automovil(models.Model):
    Patente = models.CharField(max_length=10, unique=True)
    Modelo = models.CharField(max_length=50)
   # Color = models.CharField(max_length=100)
    Anio = models.IntegerField(verbose_name= 'Añio')
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.Patente, self.Modelo, self.Anio, self.Marca)
    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"
        
