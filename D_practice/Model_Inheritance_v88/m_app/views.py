from django.shortcuts import render,HttpResponse

# Create your views here.
def showIndex(request):
    return HttpResponse("<h1>Abstract Base Model</h1>")