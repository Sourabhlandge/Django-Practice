from django.shortcuts import render

# Create your views here.
def count_view(request):
    count = int(request.COOKIES.get('count',0))
    newcount = count+1
    response = render(request,"count.html", {'count':newcount})
    #response.set_cookie('count',newcount) #used to store temp cookies
    response.set_cookie('count',newcount,max_age=20) # 20second used to store permanant cookie(Persistance cookie)
    return response
