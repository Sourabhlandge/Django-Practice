from django.contrib import admin
from django.urls import path
from wishApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dateTimeInfo),
]
