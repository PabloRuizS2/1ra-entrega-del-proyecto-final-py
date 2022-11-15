from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name= "index"),
    path('cursos/', cursos, name="cursos" ),
    path('crear_curso/', crear_curso, name="crear_curso" ),
    path('buscar_curso/', buscar_curso, name="buscar_curso"),
    path('profesores/', profesores, name="profesores"),
    path('crear_profesor/', crear_profesor, name="crear_profesor" ),
    path('buscar_profesor/', buscar_profesor, name="buscar_profesor"),
    path('alumnos/', alumnos, name="alumnos"),
    path('crear_alumno/', crear_alumno, name="crear_alumno" ),
    path('buscar_alumno/', buscar_alumno, name="buscar_alumno"),
    path('base/', base),
   
]
