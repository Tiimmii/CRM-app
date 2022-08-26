import random
from unicodedata import category
from django.shortcuts import reverse, redirect
from django.views import generic
from CRMapp.models import Agent, Category
from .forms import AgentCreationForm
from CRMapp.mixins import ManualLoginRequiredMixin
from django.core.mail import send_mail

class Agent_list(ManualLoginRequiredMixin, generic.ListView):
    template_name = 'agent-list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        # To filter the Agents based on the organisation of the authenticated user
        queryset = Agent.objects.filter(organisation = self.request.user.auto)  
        return queryset

    def form_valid(self, form):
        if not self.request.user.is_organisor:
            return redirect('leads:lead-list')
        else:
            return super(Agent_list, self).form_valid(form)

class Agent_create(ManualLoginRequiredMixin, generic.CreateView):
    template_name= 'agent-create.html'
    form_class = AgentCreationForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    #for automatically generating the organisation id and generating a random password for agent created
    def form_valid(self, form):
        user = form.save(commit=False)
        # Categorizing the created agent as an agent and not an organisor
        user.is_organisor = False
        user.is_agent = True
        # setting a random password for created agent
        user.set_password(f"{random.randint(0,100000)}")
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.auto
        )
        #sending a mail to agent from the authenticated organisor to ensure agents resets their passwords to login
        send_mail(
            subject = 'U are now an agent',
            message = 'u have been made as an agent of Timmi CRM, Please dont forget to reset ure password',
            from_email = self.request.user.email,
            recipient_list= [user.email],
        )

        return super(Agent_create,self).form_valid(form)

class Agent_update(ManualLoginRequiredMixin, generic.UpdateView):
    template_name = 'agent-update.html'
    form_class = AgentCreationForm
    queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('agents:agent-list')

class Agent_delete(ManualLoginRequiredMixin, generic.DeleteView):
    template_name = 'agent-delete.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'

    def get_success_url(self):
        return reverse('agents:agent-list')

class Agent_details(ManualLoginRequiredMixin, generic.DetailView):
    template_name = 'agent-detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agents'