from django import forms
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class LeadCreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

class LeadSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}