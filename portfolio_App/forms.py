from django import forms
from portfolio_App.models import *


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'
