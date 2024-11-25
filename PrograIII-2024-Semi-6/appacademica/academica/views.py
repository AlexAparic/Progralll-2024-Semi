from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import alumno, docente, materia
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a Programacion Computacional III")

def edad(request, edad):
    return HttpResponse("Tu edad es %s años" %edad)

def index(request):
    return render(request, 'index.html')

def vista(request, form):
    return render(request, f"{form}.html")

def consultar_alumnos(request):
    filtro = request.GET.get('q', '')
    if filtro:
        datos = alumno.objects.filter(
            Q(codigo__icontains=filtro) | 
            Q(nombre__icontains=filtro) | 
            Q(direccion__icontains=filtro) |
            Q(telefono__icontains=filtro)  
        ).values('id', 'codigo', 'nombre', 'direccion', 'telefono')
    else:
        datos = alumno.objects.values('id', 'codigo', 'nombre', 'direccion', 'telefono')
    return JsonResponse(list(datos), safe=False)

def consultar_docentes(request):
    filtro = request.GET.get('q', '')
    if filtro:
        datos = docente.objects.filter(
            Q(codigo__icontains=filtro) | 
            Q(nombre__icontains=filtro) | 
            Q(direccion__icontains=filtro) |
            Q(email__icontains=filtro) |
            Q(telefono__icontains=filtro)
        ).values('id', 'codigo', 'nombre', 'direccion', 'telefono', 'email')
    else:
        datos = docente.objects.values('id', 'codigo', 'nombre', 'direccion', 'telefono', 'email')
    return JsonResponse(list(datos), safe=False)

def consultar_materias(request):
    filtro = request.GET.get('q', '')
    if filtro:
        datos = materia.objects.filter(
            Q(codigo__icontains=filtro) | 
            Q(nombre__icontains=filtro)
        ).values('id', 'codigo', 'nombre', 'uv')
    else:
        datos = materia.objects.values('id', 'codigo', 'nombre', 'uv')
    return JsonResponse(list(datos), safe=False)


@csrf_exempt
def guardar_alumno(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        accion_realizada = ""
        
        if data.get("accion") == "nuevo":
            editAlumno = alumno.objects.create(
                codigo=data.get("codigo"),
                nombre=data.get("nombre"),
                direccion=data.get("direccion"),
                telefono=data.get("telefono"),
            )
            accion_realizada = "guardado"
        
        elif data.get("accion") == "modificar":
            editAlumno = alumno.objects.get(id=data.get("idAlumno"))
            editAlumno.codigo = data.get("codigo")
            editAlumno.nombre = data.get("nombre")
            editAlumno.direccion = data.get("direccion")
            editAlumno.telefono = data.get("telefono")
            editAlumno.save()
            accion_realizada = "modificado"
        
        elif data.get("accion") == "eliminar":
            editAlumno = alumno.objects.get(id=data.get("idAlumno"))
            editAlumno.delete()
            accion_realizada = "eliminado"
        
        return JsonResponse({'msg': 'ok', 'idAlumno': editAlumno.id, 'accion_realizada': accion_realizada})

@csrf_exempt
def guardar_docente(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        accion_realizada = ""
       
        if( data.get("accion")=="nuevo" ):
            editDocente = docente.objects.create(
                codigo = data.get("codigo"),
                nombre = data.get("nombre"),
                direccion = data.get("direccion"),
                telefono = data.get("telefono"),
                email = data.get("email"),
            )
            accion_realizada = "guardado"
            
        elif( data.get("accion")=="modificar" ):
            editDocente = docente.objects.get(id=data.get("idDocente"))
            editDocente.codigo = data.get("codigo")
            editDocente.nombre = data.get("nombre")
            editDocente.direccion = data.get("direccion")
            editDocente.telefono = data.get("telefono")
            editDocente.email = data.get("email")
            editDocente.save()
            accion_realizada = "modificado"

        elif( data.get("accion")=="eliminar" ):
            editDocente = docente.objects.get(id=data.get("idDocente"))
            editDocente.delete()
            accion_realizada = "eliminado"
        return JsonResponse({'msg':'ok', 'idDocente': editDocente.id, 'accion_realizada': accion_realizada})

@csrf_exempt
def guardar_materia(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        accion_realizada = ""
        if( data.get("accion")=="nuevo" ):
            editMateria = materia.objects.create(
                codigo = data.get("codigo"),
                nombre = data.get("nombre"),
                uv = data.get("uv"),
            )
            accion_realizada = "guardado"
        elif( data.get("accion")=="modificar" ):
            editMateria = materia.objects.get(id=data.get("idMateria"))
            editMateria.codigo = data.get("codigo")
            editMateria.nombre = data.get("nombre")
            editMateria.uv = data.get("uv")
            editMateria.save()
            accion_realizada = "modificado"

        elif( data.get("accion")=="eliminar" ):
            editMateria = materia.objects.get(id=data.get("idMateria"))
            editMateria.delete()
            accion_realizada = "eliminado"
        return JsonResponse({'msg':'ok', 'idMateria': editMateria.id,'accion_realizada': accion_realizada})
        