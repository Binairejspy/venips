
from django import forms

from acceuil.models import *

class freelance_Form(forms.ModelForm):
    
    class Meta:
        model = freelances
        fields = ('qualite','biographie','prix_jours')
       
    
        widgets = {

            
            'qualite':forms.TextInput(attrs={'class':'form-control '}),
            'biographie':forms.TextInput(attrs={'class':'form-control '}),
            'prix_jours':forms.TextInput(attrs={'class':'form-control '}),
            

           






        }

    
class concept_Form(forms.ModelForm):

    class Meta:
        model = concepts_freelance
        fields = ('img_concept','description_concept')
        

        widgets = {

            
            'img_concept':forms.FileInput(attrs={'class':'form-control '}),
            'description_concept':forms.TextInput(attrs={'class':'form-control '}),}