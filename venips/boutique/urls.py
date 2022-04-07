from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *
from acceuil.views import*
from freelance.views import *
from annonce.views import *
from connexion.views import *
from moncompte.views import moncompte


urlpatterns = [
    
    path('boutique',boutique,name='boutique'),
    path('article/boutique',boutique),
    path('boutique/chemise',chemise,name='chemise'),
    path('boutique/index',index,name='index'),
    path('boutique/chaussure',chaussures,name='chaussure'),
    path('boutique/veste',Veste,name='veste'),
    path('boutique/ordinateur',ordinateur,name='ordinateur'),
    path('boutique/voiture',voiture,name='voiture'),
    path('boutique/telephone',telephone,name='telephone'),
    path('boutique/apropos',apropos,name='apropos'),
    path('boutique/contact',contact,name='contact'),
    path('boutique/boutique',boutique,),
    path('boutique/connexion',connexion,),
    path('boutique/annonces',annonce),
    path('boutique/freelance',freelance),
    path('boutique/moncompte',moncompte,name='moncompte'),
    path('details/<int:id>',details,name='details'),
    path('details/index',index),
    path('details/boutique',boutique),
    path('details/freelance',freelance),

    path('details/contact',contact),
    path('details/annonces',annonce),
    path('details/connexion',connexion),
    path('annoncesdetails_annonce/connexion',connexion),
    path('annoncesdetails_annonce/index',index),
    path('annoncesdetails_annonce/boutique',boutique),
    path('annoncesdetails_annonce/freelance',freelance),
    path('annoncesdetails_annonce/apropos',apropos),
    path('annoncesdetails_annonce/contact',contact),
    path('annoncesdetails_annonce/annonces',annonce),
    path('annoncesdetails_annonce/inscription',inscription),
    path('details/apropos',apropos),
    path('details/moncompte',moncompte),
    path('annonces/connexion',connexion),
    path('annonces/index',index),
    path('annonces/boutique',boutique),
    path('annonces/freelance',freelance),
    path('annonces/apropos',apropos),
    path('annonces/contact',contact),
    path('annonces/annonces',annonce),

    path('recherche',recherche,name='recherche'),
    path('ajout_commande',ajout_commande,name='ajout_commande'),
    path('boutique/ajout_commande',ajout_commande,name='ajout_commande'),
    path('details/ajout_commande',ajout_commande,name='ajout_commande'),
    path('profile/ajout_commande',ajout_commande,name='ajout_commande'),
    
     


    path('panier',panier,name='panier'),
    path('suppression<int:id>',suppression,name='suppression'),
    path('felicitation',all_commande,name='felicitation'),
    path('commendez<int:id>',one_commande,name='one_commande')
    
    
]
