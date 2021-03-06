from django.shortcuts import render
from .import forms

def thanku(request):
    return render(request,"thanku.html")
# Create your views here.
def showForm(request):
    if request.method == 'GET':
       form = forms.StudentRegistrationForm()
    if request.method == 'POST':
        form = forms.StudentRegistrationForm(request.POST)
        if form.is_valid():
           print(form.cleaned_data['name'])
           print(form.cleaned_data['enroll'])
           print(form.cleaned_data['email'])
           print(form.cleaned_data['feedback'])
          # my_dict = {'name':name, 'enroll':enrollment, 'email':email1, 'feedback':feedback}
           #return thanku(request)
    return render(request, "studentRegistration.html", {'form': form})