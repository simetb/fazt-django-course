from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', hello_django, name='index'),
    path('hello/<str:username>', hello_user),
    path('project/', view_project),
    path('task/', view_tasks),
    path('task/<int:id>', view_task),
    path('create_task/', create_task)
    
 ]
