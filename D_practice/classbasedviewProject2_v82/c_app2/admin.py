from django.contrib import admin
from c_app2.models import BookModel

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'page', 'price']
admin.site.register(BookModel,BookAdmin)