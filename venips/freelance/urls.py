from django.urls import path

from freelance.views import *
from acceuil.views import*
from freelance.views import *
from annonce.views import *
from boutique.views import *
from connexion.views import *
from moncompte.views import moncompte

urlpatterns = [
    path('freelance',freelance,name='freelance'),
    path('recherche_freelance',recherche_freelance,name='recherche_freelance'),
    path("profile/<int:id>",profile,name='profile'),
    path("profile/",profile,name='profile'),
    path('profile/index',index),
    path('profile/boutique',boutique),
    path('profile/freelance',freelance),
    path('profile/apropos',apropos),
    
    path('profile/moncompte',moncompte),

    path('detals/apropos',apropos),
    path('profile/contact',contact),
    path('profile/annonces',annonce),
    path('profile/connexion',connexion),
    path('ajout',ajout,name='ajout'),
    path('ajout_concept',ajout_concept,name='ajout_concept')
    
]
