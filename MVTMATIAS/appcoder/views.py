from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):

    cursito= Curso(nombre="python", comision=34645)
    cursito.save()
    cadena_texto=f"curso guardado: nombre: {cursito.nombre}, comision: {cursito.comision}"
    return HttpResponse(cadena_texto)
