from django.shortcuts import render
from cm_app.models import Employee

# Create your views here.
def showIndex(request):
    #employees = Employee.objects.get_emp_salary_range(15000,25000)
    employees = Employee.objects.get_emp_sorted_by('ename')
    my_dict = {'employees': employees}
    return render(request, "index.html", context=my_dict)