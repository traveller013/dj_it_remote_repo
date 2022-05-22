from importlib.resources import path
from django.urls import path
from . import views
urlpatterns = [
    #need commas after every entry
    #path('' , views.index, name = "list"),
    path('',views.taskList,name = 'home')
    
]