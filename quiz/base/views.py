from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requisicao):
    return HttpResponse('Olá Mundo, em Python Django - ROTA (req,rep)! ok =D ')