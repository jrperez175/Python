from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola Mundo Desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    nombre = input("Digite su Nombre:")
    telefono = input("Digite su Telefono:")
    return HttpResponse(f'Contacto: Nombre {nombre} , Telefono {telefono}')



