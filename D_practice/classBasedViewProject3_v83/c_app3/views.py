from django.shortcuts import render
from c_app3.models import Company
#from c_app3.forms import CompanyForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    #form_class = CompanyForm()
    fields = ('name', 'location', 'ceo')
    template_name = "company_form.html"
    context_object_name = 'company_form'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'ceo')
    template_name = 'company_form.html'

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('companies')
