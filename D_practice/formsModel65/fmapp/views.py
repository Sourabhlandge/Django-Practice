from django.shortcuts import render
from fmapp import forms
from fmapp.models import Student

# Create your views here.
def showIndex(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Data inserted Successfully')
    return render(request,"studentregis.html",{'form':form})