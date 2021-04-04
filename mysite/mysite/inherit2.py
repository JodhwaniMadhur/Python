import datetime
#from django.shortcuts import render_to_response(removed in django 3.0)
from django.http import HttpResponse
from django.http import HttpResponse, request
from django.template import Template,Context
from django.shortcuts import render

#This is very very important in inheritance function,hours_offset is name mantiones 
# in double curly braces in html file and we need to assign them value here so we have to use it.
def inherit2(request,offset):
    offset=int(offset)
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html= "hours_ahead.html"
    #refering to template
    return render(request,html,{'hours_offset': offset,'next_time':dt})
    #always pass dynamic value to the render in key value pairs like dictionary 
    # that you wanna display through html