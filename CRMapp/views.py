from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead
from .forms import LeadCreationForm

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads':leads})

def lead_detail(request, pk):
    leads = Lead.objects.get(id=pk)
    return render(request, 'lead-detail.html', {'leads':leads})

def lead_create(request):
    form = LeadCreationForm()
    if request.method == 'POST':
        form = LeadCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'lead-create.html', {'form':form})


