from django import forms
from .models import Category, Lead, User, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField

class LeadCreateForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length = 20)
    age = forms.IntegerField()
    agent = forms.ModelChoiceField(queryset = Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organisation = request.user.auto)
        super(LeadCreateForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents


class LeadUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
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
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation = request.user.auto)
        super(AgentAssignForm,self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
        
class CategoryUpdateForm(forms.Form):
    category = forms.ModelChoiceField(queryset = Category.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        categories = Category.objects.filter(user = request.user)
        super(CategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = categories