from django.shortcuts import render,redirect
# Create your views here.
from acceuil.models import *
from freelance.forms import *
def freelance(request):
    free = freelances.objects.all()
    quantite_free = len(free)
    return render(request,'freelance.html',{'free':free,'qtf':quantite_free})

def recherche_freelance(request):
    qualite_saisi = request.GET['qualite']
    free_trouve =freelances.objects.filter(qualite__icontains=qualite_saisi)
    quantite_free = len(free_trouve)
    return render(request,'free_recherche.html',{'free_trouve':free_trouve,'qtf':quantite_free})


def profile(request,id):
    #chaque liason avec une autre table donne l'id de l'objet lieu donc on peut recuperer tout les objects possedant cet id
    freelance_pub = concepts_freelance.objects.filter(nomfreelance_id=id)
    #permet de recuperer que le premier element des elements dans les tables
    unique = freelance_pub.distinct()[:1]
    
  
    return render(request,'profile.html',{'freepub':freelance_pub,'unique':unique})


def ajout(request):
    if request.method =="POST":
        form = freelance_Form(request.POST)
        if form.is_valid:
            user_connect = request.user
            user_info = Clients.objects.get(nomutilisateur=user_connect)
            FA=freelances() #FA est freelance ajoute
            FA.qualite = request.POST['qualite']
            FA.biographie = request.POST['biographie']
            FA.prix_jours = request.POST['prix_jours']

            FA_ATTENDANT = form.save(commit=False) #Permet de creer un model intermediaire pour l'insertion des donneés
            FA_ATTENDANT.nomfree = user_info
            form.save()



            
            return redirect('freelance')
        else:
            form = freelance_Form()
    else:
        form =freelance_Form()
    return render(request,'ajout.html',{'form':form})


def ajout_concept(request):
    if request.method =='POST':
        form = concept_Form(request.POST,request.FILES)
        if form.is_valid:
             user_connect = request.user
             user_info = Clients.objects.get(nomutilisateur=user_connect)
            
             CF_attendant = form.save(commit=False)
             CF_attendant.nomfreelance = user_info
             form.save()
             return redirect('moncompte')
        else:
            form = concept_Form()
    else:
        form = concept_Form()
    return render(request,'ajout_concept.html',{'form':form})