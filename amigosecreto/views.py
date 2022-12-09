from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Participante
import random

def home(request):
    return render(request, "index.html")


def cadastro(request):
    if request.method == "POST":
       return redirect("add_participante")
    return render(request, "organizador/cadastro.html")


def add_participante(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        cod_participante = random.randint(1000, 9999)
        participante = Participante(cod_participante, nome)
        participante.save()
        return redirect("add_participante")

    return render(request, "organizador/add_participante.html")


def home_participante(request):
    pass
