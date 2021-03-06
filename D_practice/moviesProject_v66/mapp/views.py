from django.shortcuts import render,HttpResponseRedirect
from mapp.models import Movies
from mapp import forms
import datetime
from django.contrib import messages
from django.utils import timezone
# Create your views here.
def showIndex(request):
    dateTime = datetime.datetime.now()
    hours = int(dateTime.strftime('%H'))
    if hours>=2 and hours < 12:
        msg = "Good Morning!!!"
    elif hours>12 and hours <16:
        msg = "Good AfterNoon!!!"
    elif hours>16 and hours<20:
        msg = "Good Evening!!!"
    else:
        msg = "Good Night!!!"
    my_dict = {'date': dateTime, 'msg': msg}
    return render(request,"movies_index.html",context=my_dict)

def addmovie(request):
    form = forms.MovieForm()
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'Movie Inserted Successfully')
        return HttpResponseRedirect('/listmovies')
    else:
        return render(request, "addmovie1.html",{"form":form})


def listmovies(request):
    delete = Movies.objects.get(id=1).delete()
    listmovie  = Movies.objects.all()
    my_dict = {"listmovies":listmovie}
    return render(request,"listmovies.html",context=my_dict)