from django.shortcuts import render
from app1.models import Student,Employee
import datetime

# Create your views here.
def showIndex(request):
    dt = datetime.datetime.now()
    qs = Employee.objects.all()
    my_dict = {'date_msg': dt, 'data': qs}
    return render(request,"index.html", context=my_dict)