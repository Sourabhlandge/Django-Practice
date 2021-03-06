from django.shortcuts import render
from s_app3.forms import AddItemsForm

# Create your views here.
def add_items(request):
    form = AddItemsForm()
    if request.method=='POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(5)
        age = request.session.get_expiry_age()
        date = request.session.get_expiry_date()
        print("Age::",age)
        print("Date::",date)
    return render(request,"add_items.html", {'form':form})


def display_items(request):
    return render(request,"display_items.html")