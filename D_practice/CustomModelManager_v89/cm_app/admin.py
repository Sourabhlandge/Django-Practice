from django.contrib import admin
from cm_app.models import Employee,ProxyEmployee,ProxyEmployee2

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename', 'esalary', 'eaddress']
class ProxyAdmin(admin.ModelAdmin):
    list_display = ['eno','ename', 'esalary', 'eaddress']
class ProxyAdmin2(admin.ModelAdmin):
    list_display = ['eno','ename', 'esalary', 'eaddress']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyAdmin)
admin.site.register(ProxyEmployee2,ProxyAdmin2)