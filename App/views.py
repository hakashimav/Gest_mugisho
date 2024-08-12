from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.dao.dao_add import dao_Add
from App.dao.dao_get import dao_get
# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('index2.html')
    return HttpResponse(template.render(context, request))


def datatable(request):
    context = {}
    template = loader.get_template('datatable.html')
    return HttpResponse(template.render(context, request))



def forms(request):
    try:

        context = {}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e
    
def formSend(request):
    try:
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
            dao_Add.addClient(prenom,nom,postnom,telclient,mail,numrccm,genre,EtatciviCleint,QualClient,LieunClient)

            # # get the last id from table client
            get_idClient = dao_get.getIdClient()

            # # save the data send for dossier
            # dao_Add.addDossier(ElemDoss,AttentDoss,AvisDoss,get_idClient)

            # # save the data send for paiement
            # dao_Add.addPaiement(MontPaiem,MotifPaiem,get_idClient)


        context = {'a':prenom}
        template = loader.get_template('forms.html')
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return e