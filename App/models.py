from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Dossier(models.Model):
    ElemDoss=models.CharField(max_length=150,null=True,blank=True)
    AttentDoss=models.CharField(max_length=150,null=True,blank=True)
    AvisDoss=models.CharField(max_length=150,null=True,blank=True)
    Date_create=models.DateTimeField(auto_now_add=True)
    Date_modification = models.DateTimeField(blank=True,null=True)
    Numclient=models.ForeignKey('Client', related_name='DosCleint', null=True, blank=True, on_delete=models.CASCADE)
    NumAvocat=models.ForeignKey('Avocat', related_name='AvocDos', null=True, blank=True, on_delete=models.CASCADE)
    is_ready=models.BooleanField(default=False)
    consulter = models.BooleanField(default=False)
    traiter = models.BooleanField(default=False)
    annuler = models.BooleanField(default=False)

class EvoDossier(models.Model):
    dossier=models.ForeignKey('Dossier', related_name='dossier_evo', null=True, blank=True, on_delete=models.CASCADE)
    ElemDoss=models.CharField(max_length=150,null=True,blank=True)
    AttentDoss=models.CharField(max_length=150,null=True,blank=True)
    AvisDoss=models.CharField(max_length=150,null=True,blank=True)
    Date_create=models.DateTimeField(auto_now_add=True)
    is_ready=models.BooleanField(default=False)
    consulter = models.BooleanField(default=False)


class Client(models.Model):
    PrenonCient=models.CharField(max_length=150,null=True,blank=True)
    NomClient=models.CharField(max_length=150,null=True,blank=True)
    PostnomClient=models.CharField(max_length=150,null=True,blank=True)
    LieunClient=models.CharField(max_length=150,null=True,blank=True)
    etaClient=models.CharField(max_length=150,null=True,blank=True)
    EtatciviCleint=models.CharField(max_length=20,null=True,blank=True)
    NumClien=models.IntegerField(null=True,blank=True)
    Numrccm=models.IntegerField(null=True,blank=True)
    QualClient=models.CharField(max_length=150,null=True,blank=True)
    FaxClient=models.CharField(max_length=150,null=True,blank=True)
    Date_create=models.DateTimeField(auto_now_add=True)
    NumAct=models.ForeignKey('Acteur', related_name='ActClient', null=True, blank=True, on_delete=models.CASCADE)
    CodeNatcl=models.ForeignKey('Nationalite', related_name='NatClient', null=True, blank=True, on_delete=models.CASCADE)
    CodeCategcl=models.ForeignKey('Categorie_client', related_name='Categcl', null=True, blank=True, on_delete=models.CASCADE)



class Paiement(models.Model):
    NumPaiem=models.IntegerField(auto_created=True,null=True)
    MontPaiem=models.IntegerField()
    MotifPaiem=models.CharField(max_length=150,null=True,blank=True)
    dossier=models.ForeignKey('Dossier', related_name='dossier_paie', null=True, blank=True, on_delete=models.CASCADE)
    Date_create=models.DateTimeField(auto_now_add=True)



class Nationalite(models.Model):
    CodeNatcl=models.IntegerField(auto_created=True,null=True)
    LibNatcl=models.CharField(max_length=150,null=True,blank=True)



class Rendez_vous(models.Model):
    MotifRendez=models.CharField(max_length=150,null=True,blank=True)
    HeureRendez=models.TimeField()
    ObserRendez=models.CharField(max_length=150,null=True,blank=True)
    NumClient=models.ForeignKey('Client', related_name='RdvCleint', null=True, blank=True, on_delete=models.CASCADE)
    MatriAvoc=models.ForeignKey('Avocat', related_name='RdvAvoc', null=True, blank=True, on_delete=models.CASCADE)



class Nature_consultation(models.Model):
    CodeNatur=models.IntegerField(auto_created=True)
    DenomNatur=models.CharField(max_length=150,null=True,blank=True)



class Acteur(models.Model):
    NumAct=models.IntegerField(auto_created=True,default=True)
    NomAct=models.CharField(max_length=150,null=True,blank=True)
    PostnomAct=models.CharField(max_length=150,null=True,blank=True)
    PrenAct=models.CharField(max_length=150,null=True,blank=True)
    TelAct=models.CharField(max_length=150,null=True,blank=True)
    EmailAct=models.CharField(max_length=150,null=True,blank=True)
    utilisateur=models.ForeignKey(User,related_name="utilisateur_acteur" ,blank=True, null=True, on_delete=models.CASCADE)




class Concerner(models.Model):
    Remarquer=models.CharField(max_length=150,null=True,blank=True)
    NumConsult=models.ForeignKey('Consultation', related_name='ConsuConcer', null=True, blank=True, on_delete=models.CASCADE)
    NumDoss=models.ForeignKey('Dossier', related_name='DosConcer', null=True, blank=True, on_delete=models.CASCADE)




class Consultation(models.Model):
    NumConsult=models.IntegerField(auto_created=True)
    CodeNatur=models.ForeignKey('Nature_consultation', related_name='NaturConsult', null=True, blank=True, on_delete=models.CASCADE)
    NumPaiem=models.ForeignKey('Paiement', related_name='PaiemConsult', blank=True, on_delete=models.CASCADE)
    Date_create=models.DateTimeField(auto_now_add=True)



class Avocat(models.Model):
    MatricAvoc=models.IntegerField()
    NumAct=models.ForeignKey('Acteur', related_name='ActAvoc', null=True, blank=True, on_delete=models.CASCADE)
    NomAct=models.CharField(max_length=150,null=True,blank=True)
    PostnomAct=models.CharField(max_length=150,null=True,blank=True)
    PrenAct=models.CharField(max_length=150,null=True,blank=True)
    TelAct=models.CharField(max_length=150,null=True,blank=True)
    EmailAct=models.CharField(max_length=150,null=True,blank=True)
    utilisateur=models.ForeignKey(User,related_name="utilisateur_avocat" ,blank=True, null=True, on_delete=models.CASCADE)




class Categorie_client(models.Model):
    CodeCategcl=models.IntegerField(auto_created=True)
    LibCategcl=models.CharField(max_length=150,null=True,blank=True)

class Model_Utilisateur(models.Model):
    utilisateur=models.ForeignKey(User,related_name="utilisateur_user" ,blank=True, null=True, on_delete=models.CASCADE)
    nom=models.CharField(max_length = 50, null = True, blank = True)    
    postnom=models.CharField(max_length = 50, null = True, blank = True) 
    prenom=models.CharField(max_length = 50, null = True, blank = True) 
    sexe=models.CharField(max_length = 10, null = True, blank = True)
    telephone=models.CharField(max_length = 50, null = True, blank = True)
    date_naissance=models.DateField(null = True, blank = True)
    created=models.DateTimeField(auto_now_add=True)
    adress=models.CharField(max_length = 150, null = True, blank = True)
