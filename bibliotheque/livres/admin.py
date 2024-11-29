from django.contrib import admin

from livres.models import Emprunt, Livre

# Register your models here.
admin.site.register(Livre)
admin.site.register(Emprunt)

