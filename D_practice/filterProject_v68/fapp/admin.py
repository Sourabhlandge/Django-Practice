from django.contrib import admin
from fapp.models import FilterModel

# Register your models here.
class FilterAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'department', 'date']
admin.site.register(FilterModel,FilterAdmin)
