from django.shortcuts import render,HttpResponse
from jobapp.models import *

# Create your views here.
def showJobs(request):
    return render(request, "index.html")

def hyderabadJobs(request):
    jobs_list = HyderabadJobs.objects.order_by('id')
    my_dict = {'jobs_list':jobs_list}
    return render(request,"hydjobs.html",context=my_dict)

def chennaiJobs(request):
    jobs_list = ChennaiJobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, "chennaijobs.html", context=my_dict)

def puneJobs(request):
    jobs_list = PuneJobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, "punejobs.html", context=my_dict)
