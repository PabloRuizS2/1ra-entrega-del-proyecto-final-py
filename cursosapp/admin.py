from re import A
from django.contrib import admin

from .models import Curso
from .models import Profesor
from .models import Alumno

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'comision', 'diascurso')
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombreprofesor', 'edad', 'nivel')
    
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombrealumno', 'edad', 'cursosrealizados', 'telefono')
    
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Alumno)


