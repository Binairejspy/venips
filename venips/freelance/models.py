from django.db import models

from acceuil.models import Clients

class concept_freelance(models.Model):

    nomfreelance = models.ForeignKey(Clients, on_delete=models.CASCADE)
    img_concept = models.ImageField(upload_to="media",verbose_name='image de la conception')
    description_concept = models.TextField()
   
   
    

    def __str__(self):
        return self.nomfreelance

    