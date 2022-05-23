from importlib.resources import path
from django.urls import path
from .views import TaskCreate, TaskDetail, TaskList
from .models import Task
urlpatterns = [
    #need commas after every entry
    #path('' , views.index, name = "list"),
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'tasks' ),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
]