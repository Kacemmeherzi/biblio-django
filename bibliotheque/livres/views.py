from django.shortcuts import render

from livres.models import Livre

# Create your views here.
def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'livres.html', {'livres': livres})
def livre_listes_alt (request) : 
    livres = Livre.objects.exclude(disponible=False)
    return render(request, 'livres.html', {'livres': livres})
