from django.db import models
#required in forms , null in model 
# Create your models here.
class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    date_publication = models.DateField()
    disponible = models.BooleanField(default=True)

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    nom_emprunteur = models.CharField(max_length=255)
    date_emprunt = models.DateField(auto_now_add=True)