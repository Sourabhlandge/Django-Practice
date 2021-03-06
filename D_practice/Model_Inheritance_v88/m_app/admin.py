from django.contrib import admin
from m_app.models import Student,Teacher,ContactInfo,ContactInfo1,Student1,Teacher1,Parent,Child,Subchild

# Register your models here.
#class StudentAdmin(admin.ModelAdmin):
 #   list_display = ['name', 'email', 'address', 'rollno', 'marks']
admin.site.register(Student)
#class Teacheradmin(admin.ModelAdmin):
 #   list_display = ['name', 'email', 'address', 'rollno', 'marks', 'subject', 'salary']
admin.site.register(Teacher)
#class Contactadmin(admin.ModelAdmin):
#    list_display = ['name', 'email', 'address']
#admin.site.register(ContactInfo,Contactadmin)
admin.site.register(ContactInfo1)
admin.site.register(Student1)
admin.site.register(Teacher1)

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Subchild)