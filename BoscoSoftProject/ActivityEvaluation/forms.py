from django import forms

from .models import Answer, Activity


class AnswerForm(forms.Form):
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=Answer.CHOICES)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'description', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control '})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control datepicker'})