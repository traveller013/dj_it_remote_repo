from importlib.resources import path
from django.urls import path

#from .models import task
from .views import CustomizedLoginView, TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate,RegisterPage
    #enables logout without another template
from django.contrib.auth.views import LogoutView



urlpatterns = [#need commas after every entry
    
    path('login' , CustomizedLoginView.as_view(),  name = "login"),
    path('logout/', LogoutView.as_view(next_page= 'login'), name = 'logout'),
    path('register/', RegisterPage.as_view(), name='register'),
   
    path('',TaskList.as_view(),name = 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'tasks' ),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view() , name="task-delete"),
    
]