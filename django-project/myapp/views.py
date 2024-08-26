from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

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
    data = {
        "projects": projects
    }
    return render(request, "projects.html", data)
    # return JsonResponse(projects, safe=False)

def view_task(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"<h1>task: {task.title}</h1>")

def view_tasks(request):
    tasks = Task.objects.select_related('project').all()
    data = {
        "tasks": tasks
    }
    return render(request, "tasks.html", data)

def create_task(request):
    if request.method == 'GET':
        data = {
            "form": CreateNewTask()
        }
        return render(request, "create_task.html", data)
    elif request.method == 'POST':

        Task.objects.create(
            title=request.POST['title'], 
            description=request.POST['description'], 
            project=Project.objects.get(id=2)
        )
        return redirect('/task/')

