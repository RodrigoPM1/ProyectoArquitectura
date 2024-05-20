from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(
        max_length=200,
        validators=[RegexValidator(
            regex=r'.*\d$',
            message='La dirección debe terminar en un número.'
        )]
    )
    ciudad = models.CharField(max_length=100)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    fecha_fundacion = models.DateField()
    normas = models.FileField(upload_to='normas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    sinopsis = models.TextField()
    anio_publicacion = models.DateField()
    editorial = models.CharField(max_length=200)
    isbn = models.CharField(
        max_length=17,
        validators=[RegexValidator(
            regex=r'^\d{1,5}-\d{1,7}-\d{1,7}-\d{1,7}-\d{1,7}$',
            message='El ISBN debe tener el formato 0-7645-2641-3.'
        )]
    )
    num_ejemplares = models.IntegerField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

