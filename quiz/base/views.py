from django.shortcuts import render

# Create your views here.

def home(requisicao):
    return render(requisicao,'base/home.html')