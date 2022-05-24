from importlib.resources import path
from django.urls import path
from .views import TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate
from .models import Task
urlpatterns = [
    #need commas after every entry
    #path('' , views.index, name = "list"),
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'tasks' ),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view() , name="task-delete")
]