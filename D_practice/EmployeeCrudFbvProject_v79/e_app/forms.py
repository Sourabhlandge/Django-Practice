from django import forms
from e_app.models import Employee
class EmoplyeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
