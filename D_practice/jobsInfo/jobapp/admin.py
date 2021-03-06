from django.contrib import admin
from jobapp.models import HyderabadJobs,ChennaiJobs,PuneJobs

# Register your models here.
class HyderabadAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'mobile_no']

class ChennaiAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'mobile_no']

class PuneAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'mobile_no']

admin.site.register(HyderabadJobs, HyderabadAdmin)
admin.site.register(ChennaiJobs, ChennaiAdmin)
admin.site.register(PuneJobs, PuneAdmin)