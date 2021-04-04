import datetime
#from django.shortcuts import render_to_response(removed in django 3.0)
from django.http import HttpResponse
from django.http import HttpResponse, request
from django.template import Template,Context
from django.shortcuts import render
import MySQLdb
import os
def booklist(request):
    db=MySQLdb.connect(user='Madhur',db='mj',password='Mjdvnyc7@',host='localhost')
    cursor=db.cursor()
    cursor.execute('SELECT FirstName FROM persons ORDER BY FirstName')
    name=[row[0] for row in cursor.fetchall()]
    db.close()
    print(os.path.join(os.path.dirname(__file__), 'templates'))
    return render(request,"booklist.html",{'names':name})

    ## cheap way to use db.