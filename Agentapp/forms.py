from django import forms
from CRMapp.models import Agent

class AgentCreationForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields = (
            'user',
        )