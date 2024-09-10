"""
URL configuration for ConsultClient project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index, name="Dashboard" ),
    path('datatable/', views.datatable, name="datatable"),
    path('forms/',views.forms,name="forms"),
    path('forms-send',views.formSend,name="formSend"),
    path('forms-send/',views.formsSave,name="formsSave"),
    path('Mes-dossier/',views.mesdossier,name="mesdossier"),
    path('datatable-dossier/',views.datadossier,name="datadossier"),
    re_path(r'^dossiers/(?P<id>\w+)/$',views.rdv,name="rdv"),
    re_path(r'^data-avocat/(?P<id>\w+)/$',views.dataAvocat,name="dataAvocat"),
    re_path(r'^affecter-dossier/(?P<id>\w+)/$',views.sendDate,name="sendDate"),
    # re_path(r'^affecter-dossier/(?P<id>\w+)/$', views.sendDate,name="sendDate"),
    path('répetoire des rendez-vous/', views.Repertoire,name="repertoire"),
    path('liste des dossiers par client/',views.ListeDossierClient,name="listedossierclient"),
    path('liste des paiements effectués par client/',views.ListePaiementClient,name="listepaiementclient"),
    path('liste des dossiers reçu par période/',views.ListeDossierPeriode,name="listedossierperiode"),
    path('effectif des clients consultés par date/',views.ClientsConsulte,name="clientsconsulte"),
    path('update-dossier/',views.updateDossier,name="updateDossier"),
    path('fixer-rendez-vous/',views.fixerRdv,name="fixerRdv"),
    path('login/',views.login_view,name="login"),
    path('sing-in/',views.sign_in,name="sign_in"),
    path('log-out/',views.log_out,name="log_out"),
    re_path(r'^traiter-dossier/(?P<id>\w+)/$',views.traiteDossier,name="traiteDossier"),
    re_path(r'^annuler-dossier/(?P<id>\w+)/$',views.annulerDossier,name="annulerDossier"),
    path('enregistrement-paiement/',views.savepaie,name="savepaie")
]