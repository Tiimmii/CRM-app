from django import forms
from .models import Lead, User, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField

class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

class AgentLeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
        )

class LeadSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

class AgentAssignForm(forms.Form):
    agent=forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        agents = Agent.objects.filter(organisation = user.auto)
        super(AgentAssignForm,self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
        
