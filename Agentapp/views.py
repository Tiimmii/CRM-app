from django.shortcuts import reverse
from django.views import generic
from CRMapp.models import Agent
from .forms import AgentCreationForm
from CRMapp.mixins import LoginRequiredMixin

class Agent_list(LoginRequiredMixin, generic.ListView):
    template_name = 'agent-list.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'

class Agent_create(LoginRequiredMixin, generic.CreateView):
    template_name= 'agent-create.html'
    form_class = AgentCreationForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    #for automatically generating the organisation
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.auto
        agent.save()
        return super(Agent_create,self).form_valid(form)

class Agent_update(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agent-update.html'
    form_class = AgentCreationForm
    queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('agents:agent-list')

class Agent_delete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agent-delete.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('agents:agent-list')

class Agent_details(LoginRequiredMixin, generic.DetailView):
    template_name = 'agent-detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'