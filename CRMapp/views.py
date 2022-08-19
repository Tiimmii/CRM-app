from django.views import generic
from django.shortcuts import reverse
from .models import Lead
from .forms import LeadCreateForm, LeadSignUpForm
from django.core.mail import send_mail
from .mixins import ManualLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Lead_list(LoginRequiredMixin, generic.ListView):
    template_name = 'lead-list.html'
    context_object_name = "leads"
    
    def get_queryset(self):
        queryset = Lead.objects.all()
        if self.request.user.is_organisor:
            queryset = queryset.filter(organisation__user=self.request.user)
        elif self.request.user.is_agent:
            queryset = queryset.filter(agent__user=self.request.user)

    

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
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        agent = form.cleaned_data['agent']
        Lead.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            agent=agent,
            organisation = self.request.user.auto,
        )
        send_mail(
            subject='Lead created',
            message='Lead has been Created successfully',
            from_email='test@mail.com',
            recipient_list=['test@mail.com'],
        )
        return super(Lead_create, self).form_valid(form)

    

class Lead_update(LoginRequiredMixin, generic.UpdateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

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
    





