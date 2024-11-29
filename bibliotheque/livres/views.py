from django.shortcuts import get_object_or_404, redirect, render

from livres.forms import LivreForm
from livres.models import Livre

# Create your views here.
def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'livres.html', {'livres': livres})
def livre_listes_alt (request) : 
    livres = Livre.objects.exclude(disponible=False)
    return render(request, 'livres.html', {'livres': livres})



def create_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')  # Redirect to a page that lists all livres
    else:
        form = LivreForm()
    
    return render(request, 'createlivre.html', {'form': form})

def delete_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        livre.delete()  # Delete the Livre object
        return redirect('liste_livres')  # Redirect to the list of livres after deletion
    return render(request, 'confirm_delete.html', {'livre': livre})

def update_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')  # Redirect to the list view after updating
    else:
        form = LivreForm(instance=livre)  # Pre-fill the form with existing data

    return render(request, 'update_livre.html', {'form': form})