from django.contrib import admin
from mapp.models import Movies

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate', 'movie', 'hero', 'heroine', 'rating']
admin.site.register(Movies,MovieAdmin)
