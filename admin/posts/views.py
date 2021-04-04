from django.shortcuts import render
from .models import  Post
from django.views.generic import ListView
# Create your views here.

class HomePage(ListView):
    model=Post
    template_name='home.html'
    context_object_name='all_posts_lists'


#when we enter url of admin,django opens the admin panel and we need to insert our username and password
#then we have to create model for our admin panel in model.py and then we have to display it through admin.py
#through post and then we can create our database in admin panel,then when we go to our home,as we know we 
#need to have out app name in installed apps in settings.py,also we need to add the location of out template in
#TEMPLATES/DIRS in settings.py file and so now django knows where to look for templates,when we go to home as we have done here,
#we have added another file as urls.py in posts app here and in admin/urls.py we have given location of this urls.py
#when we goto hme the admin/urls.py searched for the appropriate location according to the url and then checks into posts/urls.py
#there we have written the path and what is to be displayed according to it,there we find that we have to render the homepage,
#the home page here now rendered from the current file i.e is views.py which renders the home.html from the templates folder.
#and the html file displays all the list of objects inserted from the admin panel as a list on the homepage.

    #last step
