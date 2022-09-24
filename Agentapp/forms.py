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
            )


class AgentUpdateForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length = 20)
    email = forms.EmailField()


    def __init__(self, *args, **kwargs):
        agent = kwargs.pop('agent')
        username = User.objects.get(username = agent.user.username)
        first_name = User.objects.get(first_name = agent.user.first_name)
        last_name = User.objects.get(last_name = agent.user.last_name)
        email = User.objects.get(email = agent.user.email)
        super(AgentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].queryset = username
        self.fields['first_name'].queryset = first_name
        self.fields['last_name'].queryset = last_name
        self.fields['email'].queryset = email
    
