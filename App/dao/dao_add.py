from App.models import *

class dao_Add(object):
    def addClient(_prenom,_nom,_postnom,_telclient,_mail,_numrccm,_genre,_EtatciviCleint,_QualClient,_LieunClient):
        try:
            ClientModels = Client(PrenonCient=_prenom,NomClient=_nom,PostnomClient=_postnom,LieunClient=_LieunClient,etaClient=_genre,EtatciviCleint=_EtatciviCleint,NumClien=_telclient,Numrccm=_numrccm,QualClient=_QualClient,FaxClient=_mail)
            ClientModels.save()
            return ClientModels
        except Exception as e:
            return e
        
    @staticmethod
    def addDossier(ElemDoss,AttentDoss,AvisDoss,numClient):
        try:
            DossierModels = Dossier(ElemDoss=ElemDoss,AttentDoss=AttentDoss,AvisDoss=AvisDoss,Numclient_id=numClient)
            DossierModels.save()
            return DossierModels
        except Exception as e:
            return e
        
    @staticmethod
    def addPaiement(MontPaiem,MotifPaiem,numClient):
        try:
            PaiementModels = Paiement(MontPaiem=MontPaiem,MotifPaiem=MotifPaiem,NumCleint_id=numClient)
            PaiementModels.save()
            return PaiementModels
        except Exception as e:
            return e