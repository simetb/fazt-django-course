from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
def hello_django(request):
    return render (request, "index.html")

def hello_user(request, username):
    data = {
        "username": username
    }
    # return HttpResponse(f"<h1>Hello, {username}!</h1>")
    return render(request, "user.html", data)

def view_project(request):
    projects = list(Project.objects.values ())
    return JsonResponse(projects, safe=False)

def view_task(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"<h1>task: {task.title}</h1>")

