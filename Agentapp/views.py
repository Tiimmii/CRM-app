import random
from django.shortcuts import reverse, redirect, render
from django.views import generic
from CRMapp.models import Agent, Category, User
from .forms import AgentCreationForm, AgentUpdateForm
from CRMapp.mixins import ManualLoginRequiredMixin
from django.core.mail import send_mail
from django.views import View

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

class Agent_update(ManualLoginRequiredMixin, View):
    def get(self, request, pk):
        agent = Agent.objects.get(pk=pk)
        user = User.objects.get(username=agent.user.username)
        return render(request, "agent-update.html", {"agent":agent, "user":user})
    
    def post(self, request, pk):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        agent = Agent.objects.get(pk=pk)
        user = User.objects.get(username = agent.user.username)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('agents:agent-list')


    # queryset = Agent.objects.all()
    # context_object_name = 'agents'

    # def get_success_url(self):
    #     return reverse('agents:agent-list')

    # def get_form_kwargs(self, **kwargs):
    #     kwargs = super(Agent_update, self).get_form_kwargs(**kwargs)
    #     kwargs.update({
    #         'agent': Agent.objects.get(id=self.kwargs["pk"])
    #     })
    #     return kwargs
    # def get_object(self, pk):
    #     return Agent.objects.get(pk=pk)
    
    # def get(self, request, pk):
    #     agent = self.get_object(pk)
    #     form = self.form_class.get_object(pk)
    #     return render(request, self.template_name, {'form': form})

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