from django.shortcuts import reverse, redirect
from django.views import generic
from CRMapp.models import Agent
from .forms import AgentCreationForm
from CRMapp.mixins import LoginRequiredMixin
from django.core.mail import send_mail

class Agent_list(LoginRequiredMixin, generic.ListView):
    template_name = 'agent-list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        queryset = Agent.objects.filter(organisation = self.request.user.auto)  
        return queryset

    def form_valid(self, form):
        if not self.request.user.is_organisor:
            return redirect('leads:lead-list')
        else:
            return super(Agent_list, self).form_valid(form)

class Agent_create(LoginRequiredMixin, generic.CreateView):
    template_name= 'agent-create.html'
    form_class = AgentCreationForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    #for automatically generating the organisation id
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organisor = False
        user.is_agent = True
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.auto
        )
        send_mail(
            subject = 'U are now an agent',
            message = 'u have been made as an agent of Timmi CRM, Please dont forget t reset ure password',
            from_email = self.request.user.email,
            recipient_list= [user.email],
        )

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