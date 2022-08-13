from django import forms
from .models import Lead

class LeadCreationForm(forms.ModelForm):
    class meta:
        model = Lead
        fields = '__all__'