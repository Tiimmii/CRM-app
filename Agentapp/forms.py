from django import forms
from CRMapp.models import User

class AgentCreationForm(forms.ModelForm):
    class Meta:
        model=User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'agent_details',
            )