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
    def getAvocat():
        try:
            return Avocat.objects.all().order_by('-id')
        except:
            return None
        
    @staticmethod
    def getDossierById(id,NumAvocat):
        try:
            dos = Dossier.objects.get(id=id)
            dos.NumAvocat_id=NumAvocat
            dos.save()
            return dos
        except:
            return None