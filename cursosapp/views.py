from django.shortcuts import redirect, render
from .models import Curso
from .models import Profesor
from .models import Alumno

def index(request):
    return render(request, "cursosapp/index.html")

def cursos(request):
    cursos = Curso.objects.all() 
    return render(request, "cursosapp/cursos.html", {"cursos": cursos})

def crear_curso(request):

    if request.method == "GET":
        return render(request, "cursosapp/formulario_curso.html", {})
    elif request.method == "POST":
        info_formulario = request.POST
        curso = Curso(nombrecurso=info_formulario["nombrecurso"], profesor=info_formulario["profesor"], comision=info_formulario["comision"], diascurso=info_formulario["diascurso"])
        curso.save()
        return redirect("cursos")
    else:
         return render(request, "cursosapp/formulario_curso.html", {})

def buscar_curso(request):

    if request.method == "POST":

        info_curso = request.POST["curso"]
        
        cursos = Curso.objects.filter(nombrecurso__icontains=info_curso).values()
        

        return render(request,"cursosapp/buscar_curso.html",{"cursos":cursos})

    else: # get y otros

        cursos =  []  #Curso.objects.all()
        
        return render(request,"cursosapp/buscar_curso.html",{"cursos":cursos})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "cursosapp/profesores.html", {"profesores": profesores} )

def crear_profesor(request):

    if request.method == "GET":
        return render(request, "cursosapp/formulario_profesor.html", {})
    elif request.method == "POST":
        info_profesor = request.POST
        curso = Profesor(nombreprofesor=info_profesor["nombreprofesor"], edad=info_profesor["edad"], nivel=info_profesor["nivel"])
        curso.save()
        return redirect("profesores")
    else:
         return render(request, "cursosapp/formulario_profesor.html", {})

def buscar_profesor(request):

    if request.method == "POST":

        info_profe = request.POST["profesor"]
        
        profesores = Profesor.objects.filter(nombreprofesor__icontains=info_profe).values()
        

        return render(request,"cursosapp/buscar_profesor.html",{"profesores":profesores})

    else: # get y otros

        profesores =  []  #Curso.objects.all()
        
        return render(request,"cursosapp/buscar_profesor.html",{"profesores":profesores})


def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "cursosapp/alumnos.html", {"alumnos": alumnos} )
 
def crear_alumno(request):

    if request.method == "GET":
        return render(request, "cursosapp/formulario_alumno.html", {})
    elif request.method == "POST":
        info_alumno = request.POST
        curso = Alumno(nombrealumno=info_alumno["nombrealumno"], edad=info_alumno["edad"], cursosrealizados=info_alumno["cursosrealizados"], telefono=info_alumno["telefono"])
        curso.save()
        return redirect("alumnos")
    else:
         return render(request, "cursosapp/formulario_alumno.html", {})

def buscar_alumno(request):

    if request.method == "POST":

        info_alum = request.POST["alumno"]
        
        alumnos = Alumno.objects.filter(nombrealumno__icontains=info_alum).values()
        

        return render(request,"cursosapp/buscar_alumno.html",{"alumnos":alumnos})

    else: # get y otros

        alumnos =  []  
        
        return render(request,"cursosapp/buscar_alumno.html",{"alumnos":alumnos})




def base(request):
    return render(request, "cursosapp/base.html", {})    



