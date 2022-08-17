from django.shortcuts import reverse
from django.views import generic
from CRMapp.models import Agent

class Agent_list(generic.ListView):
    template_name = 'agent-list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('leads:lead-list')
