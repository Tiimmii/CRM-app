from django import forms
from CRMapp.models import User
from django.contrib.auth.forms import UserCreationForm


class AgentCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
            )