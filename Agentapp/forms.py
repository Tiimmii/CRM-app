from django import forms
from CRMapp.models import User
from django.contrib.auth import get_user_model

class AgentCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'agent_details',
            )


class AgentUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'agent_details',
            )