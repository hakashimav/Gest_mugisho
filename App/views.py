from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.dao.dao_add import dao_Add
from App.dao.dao_get import dao_get
from datetime import datetime, date, timedelta, time
from django.utils import timezone

# Create your views here.

def index(request):
    context = {}
    template = loader.get_template('index2.html')
    return HttpResponse(template.render(context, request))


def datatable(request):
    try:
        getClient = dao_get.getClient()

        context = {"Client":getClient}
        template = loader.get_template('datatable.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


def mesdossier(request):
    try:
        getDossier = dao_get.getDossier()
        context = {"Dossier":getDossier}
        template = loader.get_template('mesdossier.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def datadossier(request):
    try:
        getAvocat = dao_get.getAvocat()
        getDossier = dao_get.getDossier()
        context = {"Dossier":getDossier,"Avocat":getAvocat}
        template = loader.get_template('datadossier.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return e

def sendDate(request,id):
    try:
        if request.method == "POST":
            NumAvocat = request.POST.get('NumAvocat', None)
            idDossier = request.POST.get('idDossier', None)
            data = dao_get.getDossierById(idDossier,NumAvocat)
            if data:
                getDossier = dao_get.getDossier()
                context={"Dossier":getDossier}
                template = loader.get_template('datadossier.html')
                return HttpResponse(template.render(context, request))
    except Exception as e:
        return e


def dataAvocat(request,id):
    try:
        getAvocat = dao_get.getAvocat()
        idDossier = id
        context = {'Avocat':getAvocat,"idDossier":idDossier}
        template = loader.get_template('dataAvocat.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


def forms(request):
    try:
        getClient = dao_get.getClient()

        context = {"Client":getClient}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def formSend(request):
    try:
        get_idClient = ""
        if request.method == "POST":
            # data for client
            prenom = request.POST.get('prenom', None)
            nom = request.POST.get('nom', None)
            postnom = request.POST.get('postnom', None)
            telclient = request.POST.get('telclient', None)
            mail = request.POST.get('mail', None)
            numrccm = request.POST.get('numrccm', None)
            genre = request.POST.get('genre', None)
            EtatciviCleint = request.POST.get('EtatciviCleint', None)
            QualClient = request.POST.get('QualClient', None)
            LieunClient = request.POST.get('LieunClient', None)

            # data for dossier
            ElemDoss = request.POST.get('ElemDoss', None)
            AttentDoss = request.POST.get('AttentDoss', None)
            AvisDoss = request.POST.get('AvisDoss', None)

            # data for paiement
            MontPaiem = request.POST.get('MontPaiem', None)
            MotifPaiem = request.POST.get('MotifPaiem', None)
            

            # save the data send for client
            data = dao_Add.addClients(prenom,nom,postnom,LieunClient,genre,EtatciviCleint,telclient,numrccm,QualClient,mail)
            if data:
                # # get the last id from table client
                get_idClient = dao_get.getIdClient()

            # # save the data send for dossier
            dao_Add.addDossier(ElemDoss,AttentDoss,AvisDoss,get_idClient.id)

            # # save the data send for paiement
            dao_Add.addPaiement(MontPaiem,MotifPaiem,get_idClient.id)

        getClient = dao_get.getClient()

        context = {"Client":getClient}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    

def formsSave(request):
    try:
        if request.method == "POST":
            
            ClientId = request.POST.get('Client', None)
            # data for dossier
            ElemDoss = request.POST.get('ElemDoss', None)
            AttentDoss = request.POST.get('AttentDoss', None)
            AvisDoss = request.POST.get('AvisDoss', None)

            # data for paiement
            MontPaiem = request.POST.get('MontPaiem', None)
            MotifPaiem = request.POST.get('MotifPaiem', None)
            
            # # save the data send for dossier
            dao_Add.addDossier(ElemDoss,AttentDoss,AvisDoss,ClientId)

            # # save the data send for paiement
            dao_Add.addPaiement(MontPaiem,MotifPaiem,ClientId)

        getClient = dao_get.getClient()

        context = {"Client":getClient}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def rdv(request,id):
    try:
        
        getDossier = dao_get.getDossierById(id)
        avocat = getDossier.NumAvocat.id
        client = getDossier.Numclient.id
        element = getDossier.ElemDoss
        attente = getDossier.AttentDoss
        avis = getDossier.AvisDoss
        context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':id}
        template = loader.get_template('dossier.html')
        return HttpResponse(template.render(context, request))

    except Exception as e:
        return e
    
def updateDossier(request):
    try:
        if request.method == "POST":
            ElemDoss = request.POST.get('ElemDoss', None)
            AttentDoss = request.POST.get('AttentDoss', None)
            AvisDoss = request.POST.get('AvisDoss', None)
            IdDossier = request.POST.get('IdDossier', None)
            now = timezone.now()
            
            data = dao_get.updateDossier(IdDossier,ElemDoss,AttentDoss,AvisDoss,now)

            if data:
                getDossier = dao_get.getDossierById(IdDossier)
                avocat = getDossier.NumAvocat.id
                client = getDossier.Numclient.id
                element = getDossier.ElemDoss
                attente = getDossier.AttentDoss
                avis = getDossier.AvisDoss
                succes1 = "Modification des informations sur le dossier!"
                context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':IdDossier,'succes1':succes1}
                template = loader.get_template('dossier.html')
                return HttpResponse(template.render(context, request))

    except Exception as e:
        return e
    

def fixerRdv(request):
    try:
        if request.method == "POST":
            MotifRendez = request.POST.get('MotifRendez', None)
            ObserRendez = request.POST.get('ObserRendez', None)
            HeureRendez = request.POST.get('HeureRendez', None)
            avocat = request.POST.get('avocat', None)
            client = request.POST.get('client', None)
            IdDossier = request.POST.get('IdDossier', None)
            
            data = dao_Add.addRdv(MotifRendez,ObserRendez,HeureRendez,client,avocat)

            if data:
                getDossier = dao_get.getDossierById(IdDossier)
                avocat = getDossier.NumAvocat.id
                client = getDossier.Numclient.id
                element = getDossier.ElemDoss
                attente = getDossier.AttentDoss
                avis = getDossier.AvisDoss
                succes2 = "Vous venez de fixé un rendez-vous sur ce dossier!"
                context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':IdDossier,'succes2':succes2}
                template = loader.get_template('dossier.html')
                return HttpResponse(template.render(context, request))
            

    except Exception as e:
        return e
    

# the views for out etat

def Repertoire(request):
    try:
        repertoire = dao_get.repertoire()
        context = {'repertoire':repertoire}
        template = loader.get_template('repetoire.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

def ListeDossierClient(request):
    try:
        dossier = dao_get.getDossier()
        context = {'dossier':dossier}
        template = loader.get_template('listedossiercleint.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


def ListePaiementClient(request):
    try:
        paiement = dao_get.paiement()
        context = {'paiement':paiement}
        template = loader.get_template('listepaiementclient.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def ListeDossierPeriode(request):
    try:

        dossier = dao_get.getDossier()
        context = {'dossier':dossier}
        template = loader.get_template('listedossierperiode.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def ClientsConsulte(request):
    try:

        context = {}
        template = loader.get_template('clientconsulte.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    

def login(request):
    try:
        context = {}
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

def sign_in(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            print('####')
            print(username)
            print('#####')
            print(password)
            print('####')
            context = {}
            template = loader.get_template('login.html')
            return HttpResponse(template.render(context, request))

    except Exception as e:
        return e