from django.shortcuts import render
from s_app1.forms import NameForm,GfForm,AgeForm

# Create your views here.
def name_view(request):
    form = NameForm()
    return render(request,"name.html",{'form':form})


def age_view(request):
    name = request.GET['name']
    request.session['name']=name
    form = AgeForm()
    return render(request,"age.html",{'form':form})


def gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GfForm()
    return render(request, "gf.html", {'form': form})


def result_view(request):
    gf = request.GET['gfname']
    request.session['gf'] = gf
    return render(request, "result.html")

