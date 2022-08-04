from django.db import models


# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellido = models.CharField(verbose_name='Apellidos', max_length=100)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    NumeroSeguro = models.DecimalField('NumeroSeguro', max_digits=4, decimal_places=4)
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellido = models.CharField(verbose_name='Apellidos', max_length=100)

    def __str__(self):
        return self.NumeroSeguro


class Historia(models.Model):
    IDHistoria = models.ForeignKey('Historia', verbose_name='ID Historia', on_delete=models.CASCADE)
    FechaEntrada = models.DateTimeField('FechaEntrada')
    FechaSalida = models.DateTimeField('FechaSalida')

    def __str__(self):
        return self.IDHistoria


class PacienteCama(models.Model):
    IDPacienteCama = models.ForeignKey('PacienteCama', verbose_name='ID Paciente Cama', on_delete=models.CASCADE)
    FechaAsignacion = models.DateTimeField('FechaAsignacion')
    Cama = models.DateField('Cama')

    def __str__(self):
        return self.IDPacienteCama


class Cama(models.Model):
    IDCama = models.ForeignKey('Cama', verbose_name='Cama', on_delete=models.CASCADE)
    Planta = models.DateField('Planta')

    def __str__(self):
        return self.IDCama


class Planta(models.Model):
    IDPlanta = models.ForeignKey('Planta', verbose_name='Planta', on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    NumeroCamas = models.DateField(verbose_name='Número Camas')

    def __str__(self):
        return self.IDPlanta


class VisitaMedica(models.Model):
    DiagnosticoEnfermedad = models.CharField(verbose_name='Diagnostico de Enfermedad', max_length=500)
    FechadeVisita = models.DateTimeField(verbose_name='Fecha de visita')
    Medico = models.CharField(verbose_name='Médico', max_length=100)
    PacienteCama = models.DateField(verbose_name='Paciente Cama')

    def __str__(self):
        return self.FechadeVisita
