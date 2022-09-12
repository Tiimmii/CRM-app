from django.urls import path
from .views import Agent_list, Agent_create, Agent_update, Agent_delete, Agent_details
app_name= 'agents'

urlpatterns=[
    path('agentlist/', Agent_list.as_view(), name='agent-list'),
    path('agentcreate/', Agent_create.as_view(), name='agent-create'),
    path('agentupdate/<str:pk>/', Agent_update.as_view(), name='agent-update'),
    path('agentdelete/<str:pk>/', Agent_delete.as_view(), name='agent-delete'),
    path('agentdetail/<str:pk>/', Agent_details.as_view(), name='agent-details'),

]