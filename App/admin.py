from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Dossier)
admin.site.register(models.Client)
admin.site.register(models.Paiement)
admin.site.register(models.Nationalite)
admin.site.register(models.Rendez_vous)
admin.site.register(models.Nature_consultation)
admin.site.register(models.Acteur)
admin.site.register(models.Concerner)
admin.site.register(models.Consultation)
admin.site.register(models.Avocat)
admin.site.register(models.Categorie_client)
admin.site.register(models.Model_Utilisateur)
admin.site.register(models.EvoDossier)
