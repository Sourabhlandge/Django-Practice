"""Blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_app import views
from blog_app.views import Post_list_view
app_name="blog_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/<slug:slug>/', Post_detail_view.as_view(), name="post_detail"),
    #path('share/', Mail_send_view.as_view(), ),
    path('emailsent/<int:post_id>/', views.mail_send,name="email_form"),
    path('', Post_list_view.as_view(),name='post_list'),


]
