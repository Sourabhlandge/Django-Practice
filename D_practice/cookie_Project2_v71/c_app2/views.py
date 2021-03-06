from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,"name.html")


def age_view(request):
    name = request.GET['name']
    response = render(request,"age.html")
    response.set_cookie('name',name)
    return response


def gf_view(request):
    age = request.GET['age']
    response = render(request, "gf.html")
    response.set_cookie('age', age)
    return response


def result_view(request):
    gf_name = request.GET['gf']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    response = render(request, "result.html", {'name':name, 'age':age, 'gf_name':gf_name})
    response.set_cookie('gf',gf_name)
    return response
