from django.views import generic
from django.shortcuts import reverse
from .models import Lead
from .forms import LeadCreateForm, LeadSignUpForm, AgentLeadUpdateForm
from django.core.mail import send_mail
from .mixins import ManualLoginRequiredMixin, AgentLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Lead_list(LoginRequiredMixin, generic.ListView):
    template_name = 'lead-list.html'
    context_object_name = "leads"
    #filtering the leads according to the organisor and agent
    def get_queryset(self):
        if self.request.user.is_organisor:
            queryset = Lead.objects.filter(organisation = self.request.user.auto)
        else:
            queryset = Lead.objects.filter(agent = self.request.user.agent)
        return queryset

    # getting the leads with null agents

    def get_context_data(self, **kwargs):
        context = super(Lead_list, self).get_context_data(**kwargs)
        if self.request.user.is_organisor:
            queryset=Lead.objects.filter(organisation=self.request.user.auto, agent__isnull=True)
        context.update(
            {
                'unassigned_leads':queryset,
            }
        )
        return context

    
class Lead_detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'lead-detail.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

class Lead_create(ManualLoginRequiredMixin, generic.CreateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # automatically assigning the organisation based on the user authenticated
        lead = form.save(commit=False)
        lead.organisation = self.request.user.auto
        lead.save()
        # To send a mail to the authenticated user.
        send_mail(
            subject='Lead created',
            message='Lead has been Created successfully',
            from_email='test@mail.com',
            recipient_list=['test@mail.com'],
        )
        return super(Lead_create, self).form_valid(form)

    

class Lead_update(LoginRequiredMixin, generic.UpdateView):
    # Lead update for authenticated organisor
    template_name = 'lead-update.html'
    form_class = LeadCreateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

class Agent_Lead_update(AgentLoginRequiredMixin, generic.UpdateView):
    # Lead Update for authenticated agent
    template_name = 'lead-update.html'
    form_class = AgentLeadUpdateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # To automatically get the agent based on the agent auhtenticated
        lead = form.save(commit=False)
        lead.agent = self.request.user.agent
        lead.save()
        return super(Agent_Lead_update, self).form_valid(form)


class Lead_delete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'lead-delete.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

class signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = LeadSignUpForm

    def get_success_url(self):
        return reverse('login')







