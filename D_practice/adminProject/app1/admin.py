from django.contrib import admin
from app1.models import Student, Employee
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'eadd', 'esalary']

admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)