from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta: 
        model = Pet
        fields = ["name","type","genus","age","explanation","pet_image"]


