from django import forms

from .models import Answer


class AnswerForm(forms.Form):
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=Answer.CHOICES)