from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.template import loader
from App.dao.dao_add import dao_Add
from App.dao.dao_get import dao_get
from datetime import datetime, date, timedelta, time
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import (authenticate,login,logout)
from django.shortcuts import redirect
# Create your views here.

@login_required(login_url='login')
def index(request):
    try:
        s=""
        idAv=""
        nbr4=0
        nbr=0
        nbr2=0
        nbr3=0
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        if idAvoct:
            idAv = idAvoct.id

        getAvocat = dao_get.getAvocat()
        getDossier = dao_get.getDossier()
        getDosByAvoc = dao_get.getDossierByAvocat(idAv)

        alert = dao_get.NewDossier(idAv)
        if alert:
            s = "vrai"
            nbr4 = alert.count()

        if getDosByAvoc:
            nbr=getDosByAvoc.count()

        getDossierTraiter = dao_get.getDossierTraiter(idAv)
        if getDossierTraiter:
            nbr2 = getDossierTraiter.count()

        getDossierAnnuler = dao_get.getDossierAnnuler(idAv)
        if getDossierAnnuler:
            nbr3 = getDossierAnnuler.count()

        context = {"Dossier":getDossier,"Avocat":getAvocat,'DossierAvocat':getDosByAvoc,'alert':alert,"s":s,"val4":nbr4,'val':nbr,'val2':nbr2,'val3':nbr3}
        template = loader.get_template('index2.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return e

@login_required(login_url='login')
def datatable(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        getClient = dao_get.getClient()

        context = {"Client":getClient,'alert':alert,"s":s}
        template = loader.get_template('datatable.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


@login_required(login_url='login')
def mesdossier(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        idAvoct = dao_get.getAvocatByUser(getuser)
        if idAvoct:
            idAv = idAvoct.id

        if alert:
            s = "vrai"
        getDossier = dao_get.getDossierByAvocat(idAv)

        context = {"Dossier":getDossier,'alert':alert,"s":s}
        template = loader.get_template('mesdossier.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


@login_required(login_url='login')
def datadossier(request):
    try:
        getAvocat = dao_get.getAvocat()
        getDossier = dao_get.getDossier()
        context = {"Dossier":getDossier,"Avocat":getAvocat}
        template = loader.get_template('datadossier.html')
        return HttpResponse(template.render(context, request))
    except Exception as e:
        return e


@login_required(login_url='login')
def sendDate(request,id):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        if request.method == "POST":
            NumAvocat = request.POST.get('NumAvocat', None)
            idDossier = request.POST.get('idDossier', None)
            data = dao_get.getDossierById(idDossier,NumAvocat)
            if data:
                getDossier = dao_get.getDossier()
                context={"Dossier":getDossier,'alert':alert,"s":s}
                template = loader.get_template('datadossier.html')
                return HttpResponse(template.render(context, request))
    except Exception as e:
        return e


@login_required(login_url='login')
def dataAvocat(request,id):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        getAvocat = dao_get.getAvocat()
        idDossier = id
        context = {'Avocat':getAvocat,"idDossier":idDossier,'alert':alert,"s":s}
        template = loader.get_template('dataAvocat.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

@login_required(login_url='login')
def forms(request):
    try:

        getClient = dao_get.getClient()

        context = {"Client":getClient}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

@login_required(login_url='login')
def formSend(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
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
            
            # save the data send for client
            data = dao_Add.addClients(prenom,nom,postnom,LieunClient,genre,EtatciviCleint,telclient,numrccm,QualClient,mail)
            if data:
                # # get the last id from table client
                get_idClient = dao_get.getIdClient()

            # # save the data send for dossier
            dao_Add.addDossier(ElemDoss,AttentDoss,AvisDoss,get_idClient.id)

        getClient = dao_get.getClient()

        context = {"Client":getClient,'alert':alert,"s":s}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    

@login_required(login_url='login')
def formsSave(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        if request.method == "POST":
            
            ClientId = request.POST.get('Client', None)
            # data for dossier
            ElemDoss = request.POST.get('ElemDoss', None)
            AttentDoss = request.POST.get('AttentDoss', None)
            AvisDoss = request.POST.get('AvisDoss', None)

            # # save the data send for dossier
            dao_Add.addDossier(ElemDoss,AttentDoss,AvisDoss,ClientId)

        getClient = dao_get.getClient()

        context = {"Client":getClient,'alert':alert,"s":s}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def savepaie(request):
    try:
        if request.method == "POST":
            MontPaiem = request.POST.get('MontPaiem', None)
            MotifPaiem = request.POST.get('MotifPaiem', None)
            IdDossier = request.POST.get('IdDossier', None)
            dao_Add.savepaei(MontPaiem,MotifPaiem,IdDossier)

        return redirect('rdv',IdDossier)

    except Exception as e:
        return e

@login_required(login_url='login')
def rdv(request,id):
    try:
        s=""

        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        
        getDossier = dao_get.getDossierById(id)
        getEvoDossier = dao_get.getDossierEvo(id)
        dao_get.views_dossier(id)
        avocat = getDossier.NumAvocat.id
        client = getDossier.Numclient.id
        if getEvoDossier:
            element = getEvoDossier.ElemDoss
            attente = getEvoDossier.AttentDoss
            avis = getEvoDossier.AvisDoss
        else:
            element = getDossier.ElemDoss
            attente = getDossier.AttentDoss
            avis = getDossier.AvisDoss

        filterDossier = dao_get.FilterDossierById(id)

        context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':id,'DossierAvocat':filterDossier,'alert':alert,"s":s}
        template = loader.get_template('dossier.html')
        return HttpResponse(template.render(context, request))

    except Exception as e:
        return e


@login_required(login_url='login')  
def updateDossier(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        if request.method == "POST":
            ElemDoss = request.POST.get('ElemDoss', None)
            AttentDoss = request.POST.get('AttentDoss', None)
            AvisDoss = request.POST.get('AvisDoss', None)
            IdDossier = request.POST.get('IdDossier', None)
            
            data = dao_get.updateDossier(IdDossier,ElemDoss,AttentDoss,AvisDoss)

            if data:
                getDossier = dao_get.getDossierById(IdDossier)
                getEvoDossier = dao_get.getDossierEvo(IdDossier)
                avocat = getDossier.NumAvocat.id
                client = getDossier.Numclient.id
                if getEvoDossier:
                    element = getEvoDossier.ElemDoss
                    attente = getEvoDossier.AttentDoss
                    avis = getEvoDossier.AvisDoss
                else:
                    element = getDossier.ElemDoss
                    attente = getDossier.AttentDoss
                    avis = getDossier.AvisDoss
                filterDossier = dao_get.FilterDossierById(IdDossier)
                succes1 = "Modification des informations sur le dossier!"
                context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':IdDossier,'succes1':succes1,'DossierAvocat':filterDossier,'alert':alert,"s":s}
                template = loader.get_template('dossier.html')
                return HttpResponse(template.render(context, request))

    except Exception as e:
        return e
    

@login_required(login_url='login')
def fixerRdv(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
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
                getEvoDossier = dao_get.getDossierEvo(IdDossier)
                avocat = getDossier.NumAvocat.id
                client = getDossier.Numclient.id
                if getEvoDossier:
                    element = getEvoDossier.ElemDoss
                    attente = getEvoDossier.AttentDoss
                    avis = getEvoDossier.AvisDoss
                else:
                    element = getDossier.ElemDoss
                    attente = getDossier.AttentDoss
                    avis = getDossier.AvisDoss
                filterDossier = dao_get.FilterDossierById(IdDossier)
                succes2 = "Vous venez de fixé un rendez-vous sur ce dossier!"
                context = {'avocat':avocat,'client':client,'element':element,'attente':attente,'avis':avis,'idDossier':IdDossier,'succes2':succes2,'DossierAvocat':filterDossier,'alert':alert,"s":s}
                template = loader.get_template('dossier.html')
                return HttpResponse(template.render(context, request))
            

    except Exception as e:
        return e
    

# the views for out etat

@login_required(login_url='login')
def Repertoire(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        repertoire = dao_get.repertoire()
        context = {'repertoire':repertoire,'alert':alert,"s":s}
        template = loader.get_template('repetoire.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

@login_required(login_url='login')
def ListeDossierClient(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        dossier = dao_get.getDossier()
        context = {'dossier':dossier,'alert':alert,"s":s}
        template = loader.get_template('listedossiercleint.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


@login_required(login_url='login')
def ListePaiementClient(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        paiement = dao_get.paiement()
        context = {'paiement':paiement,'alert':alert,"s":s}
        template = loader.get_template('listepaiementclient.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


@login_required(login_url='login')
def ListeDossierPeriode(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"

        dossier = dao_get.getDossier()
        context = {'dossier':dossier,'alert':alert,"s":s}
        template = loader.get_template('listedossierperiode.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e


@login_required(login_url='login')
def ClientsConsulte(request):
    try:
        s=""
        getuser = request.user.id
        idAvoct = dao_get.getAvocatByUser(getuser)
        alert = dao_get.NewDossier(idAvoct.id)
        if alert:
            s = "vrai"
        context = {'alert':alert,"s":s}
        template = loader.get_template('clientconsulte.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    

def login_view(request):
    try:
        context = {}
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e

def sign_in(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            # if user is not None:

            login(request,user)
            if user.is_authenticated:
                #-----------------  user ----------------------
                getuser_id=user.id                    #
                username= dao_get.getUtilisateur(getuser_id) #
                #----------------- / user ---------------------            
            else:
                raise Exception

            return redirect('Dashboard')

    except Exception as e:
        context = {
            'error':"Identifiants incorrects "+str(e),
        }
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))
    
def log_out(request):
    logout(request)

    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='login')
def traiteDossier(request,id):
    try:
        dao_get.traiterDossier(id)

        return HttpResponseRedirect(reverse('Dashboard'))

    except Exception as e:
        return None


@login_required(login_url='login')   
def annulerDossier(request,id):
    try:
        dao_get.annulerDossier(id)

        return HttpResponseRedirect(reverse('Dashboard'))

    except Exception as e:
        return None