from django.db import models

# Create your models here.

class Dossier(models.Model):
    NumDoss=models.IntegerField(auto_created=True)
    ElemDoss=models.CharField(max_length=150,null=True,blank=True)
    AttentDoss=models.CharField(max_length=150,null=True,blank=True)
    AvisDoss=models.CharField(max_length=150,null=True,blank=True)
    Date_create=models.DateTimeField(auto_now_add=True)
    Numclient=models.ForeignKey('Client', related_name='DosCleint', null=True, blank=True, on_delete=models.CASCADE)



class Client(models.Model):
    NumCleint=models.IntegerField(auto_created=True)
    EtatciviCleint=models.CharField(max_length=20,null=True,blank=True)
    NomClient=models.CharField(max_length=150,null=True,blank=True)
    PostnomClient=models.CharField(max_length=150,null=True,blank=True)
    PrenonCient=models.CharField(max_length=150,null=True,blank=True)
    LieunClient=models.CharField(max_length=150,null=True,blank=True)
    etaClient=models.CharField(max_length=150,null=True,blank=True)
    telClien=models.IntegerField()
    Numrccm=models.IntegerField()
    QualClient=models.CharField(max_length=150,null=True,blank=True)
    FaxClient=models.IntegerField()
    Date_create=models.DateTimeField(auto_now_add=True)
    NumAct=models.ForeignKey('Acteur', related_name='ActClient', null=True, blank=True, on_delete=models.CASCADE)
    CodeNatcl=models.ForeignKey('Nationalite', related_name='NatClient', null=True, blank=True, on_delete=models.CASCADE)
    CodeCategcl=models.ForeignKey('Categorie_client', related_name='Categcl', null=True, blank=True, on_delete=models.CASCADE)



class Paiement(models.Model):
    NumPaiem=models.IntegerField(auto_created=True)
    MontPaiem=models.IntegerField()
    MotifPaiem=models.CharField(max_length=150,null=True,blank=True)
    NumCleint=models.ForeignKey('Client', related_name='PaiemCleint', null=True, blank=True, on_delete=models.CASCADE)



class Nationalite(models.Model):
    CodeNatcl=models.IntegerField(auto_created=True)
    LibNatcl=models.CharField(max_length=150,null=True,blank=True)



class Rendez_vous(models.Model):
    NumRendez=models.IntegerField(auto_created=True)
    MotifRendez=models.CharField(max_length=150,null=True,blank=True)
    HeureRendez=models.TimeField()
    ObserRendez=models.CharField(max_length=150,null=True,blank=True)
    NumClient=models.ForeignKey('Client', related_name='RdvCleint', null=True, blank=True, on_delete=models.CASCADE)
    MatriAvoc=models.ForeignKey('Avocat', related_name='RdvAvoc', null=True, blank=True, on_delete=models.CASCADE)



class Nature_consultation(models.Model):
    CodeNatur=models.IntegerField(auto_created=True)
    DenomNatur=models.CharField(max_length=150,null=True,blank=True)



class Acteur(models.Model):
    NumAct=models.IntegerField(auto_created=True)
    NomAct=models.CharField(max_length=150,null=True,blank=True)
    PostnomAct=models.CharField(max_length=150,null=True,blank=True)
    PrenAct=models.CharField(max_length=150,null=True,blank=True)
    TelAct=models.CharField(max_length=150,null=True,blank=True)
    EmailAct=models.CharField(max_length=150,null=True,blank=True)



class Concerner(models.Model):
    Remarquer=models.CharField(max_length=150,null=True,blank=True)
    NumConsult=models.ForeignKey('Consultation', related_name='ConsuConcer', null=True, blank=True, on_delete=models.CASCADE)
    NumDoss=models.ForeignKey('Dossier', related_name='DosConcer', null=True, blank=True, on_delete=models.CASCADE)




class Consultation(models.Model):
    NumConsult=models.IntegerField(auto_created=True)
    CodeNatur=models.ForeignKey('Nature_consultation', related_name='NaturConsult', null=True, blank=True, on_delete=models.CASCADE)
    NumPaiem=models.ForeignKey('Paiement', related_name='PaiemConsult', null=True, blank=True, on_delete=models.CASCADE)
    Date_create=models.DateTimeField(auto_now_add=True)



class Avocat(models.Model):
    MatricAvoc=models.IntegerField()
    NumAct=models.ForeignKey('Acteur', related_name='ActAvoc', null=True, blank=True, on_delete=models.CASCADE)
    NomAct=models.CharField(max_length=150,null=True,blank=True)
    PostnomAct=models.CharField(max_length=150,null=True,blank=True)
    PrenAct=models.CharField(max_length=150,null=True,blank=True)
    TelAct=models.CharField(max_length=150,null=True,blank=True)
    EmailAct=models.CharField(max_length=150,null=True,blank=True)



class Categorie_client(models.Model):
    CodeCategcl=models.IntegerField(auto_created=True)
    LibCategcl=models.CharField(max_length=150,null=True,blank=True)