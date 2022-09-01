from django.views import generic
from django.shortcuts import reverse, redirect
from .models import Lead, Category
from .forms import LeadCreateForm, LeadSignUpForm, AgentLeadUpdateForm, AgentAssignForm,LeadUpdateForm, CategoryUpdateForm
from django.core.mail import send_mail
from .mixins import ManualLoginRequiredMixin, AgentLoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Landing_page(generic.TemplateView):
    template_name = 'registration/landing-page.html'

class Lead_list(LoginRequiredMixin, generic.ListView):
    template_name = 'lead-list.html'
    context_object_name = "leads"
    #filtering the leads according to the organisor and agent
    def get_queryset(self):
        if self.request.user.is_organisor:
            queryset = Lead.objects.filter(organisation = self.request.user.auto, agent__isnull=False)
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

class Lead_create(ManualLoginRequiredMixin, generic.FormView):
    template_name = 'lead-create.html'
    form_class = LeadCreateForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Lead_create, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs

    def form_valid(self, form):
        # automatically assigning the organisation based on the user authenticated
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        age = form.cleaned_data['age']
        agent = form.cleaned_data['agent']
        Lead.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            agent=agent,
            organisation=self.request.user.auto
        )
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
    form_class = LeadUpdateForm
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    

    def get_success_url(self):
        return reverse('leads:lead-detail', kwargs = {'pk':self.get_object().id})

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

    def form_valid(self, form):
        if form.is_valid():
            organisor = form.save(commit = False)
            organisor.save()
            Category.objects.create(name = 'contacted', user = organisor)
            Category.objects.create(name = 'unconverted', user = organisor)
            Category.objects.create(name = 'converted', user = organisor)

        return super(signup, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('leads:lead-list')
        return super(signup, self).get(*args, **kwargs)


class Agent_assign(ManualLoginRequiredMixin, generic.FormView):
    template_name = 'agent-assign.html'
    form_class = AgentAssignForm

    def get_success_url(self):
        return reverse('leads:lead-list')


    def get_form_kwargs(self, **kwargs):
        kwargs = super(Agent_assign,self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(Agent_assign, self).form_valid(form)


class Lead_categories(ManualLoginRequiredMixin, generic.ListView):
    template_name = 'lead-categories.html'
    context_object_name = 'category'

    def get_queryset(self):
        if self.request.user.is_organisor:
            queryset = Category.objects.filter(user = self.request.user)
        return queryset

class Lead_category_Detail(ManualLoginRequiredMixin, generic.DetailView):
    template_name = 'category-detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        if self.request.user.is_organisor:
            queryset = Category.objects.filter(user = self.request.user)
        return queryset

class New_lead_category(ManualLoginRequiredMixin, generic.ListView):
    template_name = 'new_lead_category.html'

    def get_queryset(self):
        if self.request.user.is_organisor:
            queryset = Category.objects.filter(user = self.request.user)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super(New_lead_category, self).get_context_data(**kwargs)
        if self.request.user.is_organisor:
            queryset = Lead.objects.filter(organisation = self.request.user.auto)
        context.update({
            'new_leads':queryset.filter(category__isnull=True),

        })
        return context
    
class Lead_category_update(ManualLoginRequiredMixin, generic.FormView):
    template_name = 'category-update.html'
    form_class = CategoryUpdateForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(Lead_category_update, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request':self.request
        })
        return kwargs

    def form_valid(self, form):
        category = form.cleaned_data['category']
        lead = Lead.objects.get(id = self.kwargs['pk'])
        lead.category = category
        lead.save()
        return super(Lead_category_update, self).form_valid(form)

    def get_success_url(self):
        return reverse ('leads:category')









