from django.urls import path
from .views import *
from acceuil.views import *
from boutique.views import *
from freelance.views import *
from annonce.views import *
from connexion.views import *



urlpatterns = [
    path('',annonce,name='annonce'),
    path('<str:element_annonce>',menu_annonces,name='filter_annonce'),
    path('details_annonce/<int:id>',details_annonce,name='details_annonce'),
    path('recherche_annonce/',recherche_annonce,name='recherche_annonce'),
    path('recherche_annonce/connexion',connexion),
    path('recherche_annonce/index',index),
    path('recherche_annonce/boutique',boutique),
    path('recherche_annonce/freelance',freelance),
    path('recherche_annonce/apropos',apropos),
    path('recherche_annonce/contact',contact),
    path('recherche_annonce/annonces',annonce),
    path('/ajout_annonce',ajout_annonce,name='ajout_annonce')
    
    
]
