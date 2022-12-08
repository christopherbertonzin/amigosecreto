from django.urls import path
from .views import *

urlpatterns = [
    path('', view=home),
    path('cadastro/', view=cadastro, name="cadastro"),
    path('cadastro/add-participante', view=add_participante, name="add_participante")
]