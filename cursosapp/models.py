from unittest.util import _MAX_LENGTH
from django.db import models

class Curso(models.Model):
    nombrecurso = models.CharField("Nombre del Curso", max_length=30)
    profesor = models.CharField("Nombre del Profesor", max_length=30)
    comision = models.PositiveIntegerField("Comision")
    diascurso = models.CharField("Dias de cursada", max_length=30)
    
class Profesor(models.Model):
    nombreprofesor = models.CharField("Nombre del profesor", max_length= 35)
    edad = models.PositiveSmallIntegerField("Edad del Profesor")
    NIVELES =(
        (1, "Basico"),
        (2, "Intermedio"),
        (3, "Avanzado")
    )
    nivel = models.PositiveSmallIntegerField("Nivel", choices= NIVELES)
    
class Alumno(models.Model):
    nombrealumno = models.CharField("Nombre del alumno", max_length= 35)
    edad = models.PositiveSmallIntegerField("Edad del Alumno")
    cursosrealizados = models.PositiveSmallIntegerField("Cursos Realizados")
    telefono = models.PositiveIntegerField("Numero telefonico alumno")
    
    
