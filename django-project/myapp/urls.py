from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', hello_django),
    path('hello/<str:username>', hello_user),
    path('project/', view_project),
    path('task /<int:id>', view_task)
    
 ]
