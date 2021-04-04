import datetime
#from django.shortcuts import render_to_response(removed in django 3.0)
from django.http import HttpResponse
from django.http import HttpResponse, request
from django.template import Template,Context
from django.shortcuts import render




def inherit(request):
    now = datetime.datetime.now()
    return render(request,"currentdatetime.html",context={'current_date': now})


    