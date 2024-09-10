from App.models import *

class dao_Add(object):
        
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
        
    @staticmethod
    def addClients(_PrenonCient,_NomClient,_PostnomClient,_LieunClient,_etaClient,_EtatciviCleint,_NumClien,_Numrccm,_QualClient,_FaxClient):
        try:
            ClientModels = Client(PrenonCient=_PrenonCient,NomClient=_NomClient,PostnomClient=_PostnomClient,LieunClient=_LieunClient,etaClient=_etaClient,EtatciviCleint=_EtatciviCleint,NumClien=_NumClien,Numrccm=_Numrccm,QualClient=_QualClient,FaxClient=_FaxClient)
            ClientModels.save()
            return ClientModels
        except Exception as e:
            return e
        

    @staticmethod
    def addRdv(Motif,observe,heur,NumCl,avoc):
        try:
            rdv = Rendez_vous(MotifRendez=Motif,ObserRendez=observe,HeureRendez=heur,NumClient_id=NumCl,MatriAvoc_id=avoc)
            rdv.save()
            return rdv
        except Exception as e:
            return e
        
    @staticmethod
    def savepaei(mont,motif,dossier):
        try:
            paie = Paiement(MontPaiem=mont,MotifPaiem=motif,dossier_id=dossier)
            paie.save()
            return paie
        except:
            return None