from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - ({self.parentesco})"

#class Compra(models.Model):
#    descripcion = models.CharField()
#    precio = models.FloatField()
#    cantidad = models.IntegerField()

#    def __str__(self):
#        return self.descripcion

class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    horario = models.TimeField()
    precio = models.FloatField()

    def __str__(self):
        return f"Vuelo de {self.origen} a {self.destino} - ${self.precio}"

class Compra(models.Model):
    descripcion = models.CharField(max_length=20)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.descripcion