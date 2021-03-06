from django.shortcuts import render

# Create your views here.
def showHome(request):
    return render(request, "home.html")


def movies_views(request):
    return render(request,"movie.html")


def politics_views(request):
    return render(request, "political.html")


def sports_views(request):
    return render(request, "sports.html")