from django.views import generic
from django.shortcuts import reverse
from .models import Lead
from .forms import LeadCreateForm
from django.core.mail import send_mail

class Lead_list(generic.ListView):
    template_name = 'lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

class Lead_detail(generic.DetailView):
    template_name = 'lead-detail.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

class Lead_create(generic.CreateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        send_mail(
            subject='Lead created',
            message='Lead has been Created successfully',
            from_email='test@mail.com',
            recipient_list='test@mail.com',
        )
        return super(Lead_create, self).form_valid(form)

    

class Lead_update(generic.UpdateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

class Lead_delete(generic.DeleteView):
    template_name = 'lead-delete.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')
    





