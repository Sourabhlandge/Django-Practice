from django import forms
from c_app3.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'