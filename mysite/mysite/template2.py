import datetime
#from django.shortcuts import render_to_response(removed in django 3.0)
from django.http import HttpResponse
from django.http import HttpResponse, request
from django.template import Template,Context
from django.shortcuts import render


def template2(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")    
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

#def template3(request):
    #now =datetime.datetime.now()
    #return render_to_response('currentdatetime.html',{'current_date': now})
    #render_to_response does not work now since it is removed after django 3.0
