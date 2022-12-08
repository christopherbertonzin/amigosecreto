from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")


def cadastro(request):
    if request.method == "POST":
        redirect("add_participante")
    return render(request, "organizador/cadastro.html")


def add_participante(request):
    return render(request, "cadastro.html")


def del_participante(request):
    pass


def home_participante(request):
    pass


def add_presente(request):
    pass


def sortear(request):
    pass