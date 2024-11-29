from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.liste_livres, name='liste_livres'),
]