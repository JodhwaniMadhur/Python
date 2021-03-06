"""mysite URL Configuration

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
from mysite.views import current_datetime,hours_ahead
from mysite.template1 import template
from mysite.template2 import template2
from mysite.inherit import inherit
from mysite.inherit2 import inherit2
from mysite.databaseconnection import booklist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/',current_datetime),
    path('time/plus/<int:offset>/',hours_ahead),#regular expression as in (\d{1,2})didn't work here so i made it <int:offset>
    path('temp/basic',template),
    path('temp/lists',template2),
    path('inherit',inherit),
    path('inherit/<int:offset>',inherit2),
    path('db',booklist),
]
