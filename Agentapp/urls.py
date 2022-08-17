from django.urls import path
from .views import Agent_list

app_name= 'agents'

urlpatterns=[
    path('agentlist/', Agent_list.as_view(), name='agent-list'),
]