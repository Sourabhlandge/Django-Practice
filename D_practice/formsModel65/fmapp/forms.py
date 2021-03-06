from django import forms
from fmapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"