from django.shortcuts import render,HttpResponse

# Create your views here.
def showIndex(request):
    print('This line printed by views function')
    print(10/0)
    return HttpResponse("<h1>Custom Middleware</h1>")