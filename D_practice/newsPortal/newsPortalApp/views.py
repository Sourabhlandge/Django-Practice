from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"news.html")
def moviesInfo(request):
    messHead = "Latest Movies Updates.. "
    mess1 = "Movies Updates1.. "
    mess2 = "Movies Updates2.. "
    mess3 = "Movies Updates3.. "
    my_dict = {"messHead":messHead, "mess1":mess1, "mess2":mess2,"mess3":mess3}
    return render(request,"newsUpdates.html",context=my_dict)

def sportsInfo(request):
    messHead = "Latest Sports Updates.. "
    mess1 = "Sports Updates1.. "
    mess2 = "Sports Updates2.. "
    mess3 = "Sports Updates3.. "
    my_dict = {"messHead":messHead,"mess1":mess1,"mess2":mess2,"mess3":mess3}
    return render(request,"newsUpdates.html",context=my_dict)

def politicalsInfo(request):
    messHead = "Latest Political Updates.. "
    mess1 = "Political Updates1.. "
    mess2 = "Political Updates2.. "
    mess3 = "Political Updates3.. "
    my_dict = {"messHead":messHead,"mess1":mess1,"mess2":mess2,"mess3":mess3}
    return render(request,"newsUpdates.html",context=my_dict)
