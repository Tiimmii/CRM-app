from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse
from .models import Lead
from .forms import LeadCreateForm

class Lead_list(ListView):
    template_name = 'lead-list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

class Lead_detail(DetailView):
    template_name = 'lead-detail.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

class Lead_create(CreateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead-list')

class Lead_update(UpdateView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')

class Lead_delete(DeleteView):
    template_name = 'lead-delete.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_success_url(self):
        return reverse('leads:lead-list')
    





