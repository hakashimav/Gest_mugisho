from App.models import *

class dao_get(object):
    @staticmethod
    def getIdClient():
        try:
            return Client.objects.all().last()
        except:
            return None
        
    @staticmethod
    def getClient():
        try:
            return Client.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def getDossier():
        try:
            return Dossier.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def getDossierByAvocat(id):
        try:
            return Dossier.objects.filter(NumAvocat_id=id).order_by('-id')
        except:
            return None
        
            
    @staticmethod
    def getAvocat():
        try:
            return Avocat.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def getAvocatByUser(id):
        try:
            return Avocat.objects.get(utilisateur_id=id)
        except:
            return None
        
    @staticmethod
    def getDossierById(id,NumAvocat):
        try:
            dos = Dossier.objects.get(id=id)
            dos.NumAvocat_id=NumAvocat
            dos.is_ready = True
            dos.save()
            return dos
        except:
            return None
        
    @staticmethod
    def repertoire():
        try:
            return Rendez_vous.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def paiement():
        try:
            return Paiement.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def getDossierById(id):
        try:
            return Dossier.objects.get(id=id)
        except:
            return None
        
    @staticmethod
    def updateDossier(idDossier,element,attent,avis,now):
        try:
            dos = Dossier.objects.get(id=idDossier)
            dos.ElemDoss = element
            dos.AttentDoss = attent
            dos.AvisDoss = avis
            dos.Date_modification = now
            dos.save()
            return dos

        except:
            return None
        
    @staticmethod
    def getUtilisateur(id):
        try:
            getuser_id=User.objects.get(id=id)
            utilisateur = Model_Utilisateur.objects.filter(utilisateur=getuser_id.id)
            for user in utilisateur:
                return user
        except Exception as e:
            print("IL Y A PAS D'UTILISATEUR AVEC CETTE IDENTIFIANT  Backend((getUtilisateur)) err=",e)