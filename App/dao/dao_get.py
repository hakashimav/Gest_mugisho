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
            return Client.objects.all()
        except:
            return None
        
    @staticmethod
    def getDossier():
        try:
            return Dossier.objects.all()
        except:
            return None