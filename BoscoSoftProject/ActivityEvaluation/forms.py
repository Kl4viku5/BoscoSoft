from django import forms

from .models import Individual

class SearchIndividualForm(forms.ModelForm):
    model = Individual
    name = forms.CharField(max_length=128, help_text="Veuillez entrer le nom.")
    age = forms.IntegerField(widget=forms.HiddenInput, initial=0)
