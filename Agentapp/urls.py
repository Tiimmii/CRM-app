from django.urls import path
from .views import Agent_list, Agent_create

app_name= 'agents'

urlpatterns=[
    path('agentlist/', Agent_list.as_view(), name='agent-list'),
    path('agentcreate/', Agent_create.as_view(), name='agent-create'),
]