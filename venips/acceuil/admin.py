from django.contrib import admin
from .models import *
from annonce.models import Annonces
from boutique.models import *


# Register your models he


admin.site.register(Clients)
admin.site.register(Annonces)
admin.site.register(Article)
admin.site.register(freelances)
admin.site.register(concepts_freelance)
admin.site.register(commandes)









