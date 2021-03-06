from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse("<h1>This Is Class Based View</h1")
class HelloWorldTemplateView(TemplateView):
    template_name = 'index.html'


class HelloWorldTemplateContext(TemplateView):
    template_name = "info.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sourabh'
        context['subject'] = 'Python'
        context['marks'] = 100
        return context