from django.shortcuts import render,redirect
from e_app.models import Employee
from e_app.forms import EmoplyeeForm
# Create your views here.

def retrieve_view(request):
    employees = Employee.objects.all()
    my_dict = {'employees':employees}
    return render(request,"index.html",context=my_dict)


def create_view(request):
    form = EmoplyeeForm()
    if request.method == 'POST':
        form = EmoplyeeForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"index.html")
    return render(request,"create.html",{'form':form})


def delete_view(request):
    eid = request.GET.get("id")
    employee = Employee.objects.filter(id=eid).delete()
    return redirect('/')

def update(request):
    update_id = request.POST.get("u_id")
    employee = Employee.objects.get(id=update_id)
    my_dict = {'employee':employee}
    return render(request,"update.html", context=my_dict)


def save_update_view(request):
    eno = request.POST.get("eno")
    ename = request.POST.get("ename")
    esal = request.POST.get("esal")
    eadd = request.POST.get("eadd")
    updated_employee = Employee(eno=eno, ename=ename, esalary=esal, eaddress=eadd).save()
    employees = Employee.objects.all()
    my_dict = {'employees': employees}
    return render(request, "index.html", context=my_dict)