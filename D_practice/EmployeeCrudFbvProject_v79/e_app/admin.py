from django.contrib import admin
from e_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esalary', 'eaddress']
admin.site.register(Employee,EmployeeAdmin)
