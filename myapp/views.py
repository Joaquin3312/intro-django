from django.http import HttpResponse
from .models import Project
from .models import Task
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
    
def hello(request, username):
    return HttpResponse("<h1>SEXOOOOO %s</h1>" %username )

def about(request):
    return render(request,'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request,'tasks/tasks.html',{
        'tasks': tasks
    })
    
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        form = CreateNewTask(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                project_id=form.cleaned_data['project'].id  # Guardar el project_id
            )
            return redirect('tasks')
        else:
            return render(request, 'tasks/create_task.html', {
                'form': form,
            })
         
   
def delete_task(request, id):
    task = Task.objects.get(id=id)
    try:
        task.delete()
        messages.success(request, 'Task deleted successfully!')
    except Exception as e:
        messages.error(request, 'Failed to delete task: %s' % e)
    return redirect('tasks')


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    projects = Project.objects.all()
    if request.method == "POST":
        try:
            task.title = request.POST["title"]
            task.description = request.POST["description"]
            task.completed = 'completed' in request.POST  # Verificar si el checkbox está marcado
            task.project_id = request.POST["project"] # 'project' ya recupera el id desde el html gracias a "projects" (ver variable arriba)
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks')
        except Exception as e:
            messages.error(request, 'Failed to update task: %s' % e)
    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'projects': projects
    })

def complete_task(request, id):
    task = Task.objects.get(id=id)
    try:
        task.completed = request.POST['completed']
        task.save()
    except Exception as e:
        print(f"error: {e}")
    return redirect('tasks')


# TASKS METHODS:

def create_project(request):
    if request.method == "GET":
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:      
        Project.objects.create(name=request.POST["name"])
        return redirect('projects') # redirect ('/projects/) ocasianaba el problema, específicamente: "/" al final de projects


def edit_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        try:
            project.name = request.POST["name"]
            project.save()
            messages.success(request, 'Project updated successfully!')
        except Exception as e:
            messages.error(request, 'Failed to update project: %s' % e)
        return redirect('projects')
    else:
        return render(request, 'projects/edit_project.html', {
            'project': project,
        })


def delete_project(request, id):
    project = Project.objects.get(id=id)
    try:
        project.delete()
        messages.success(request, 'Project deleted successfully!')
    except Exception as e:
        messages.error(request, 'Failed to delete project: %s' % e)
    return redirect('projects')

        
def detail_project(request,id):
    print(id)
    project = get_object_or_404(Project, id=id)
    # Método filter para "filtrar datos"
    tasks = Task.objects.filter(project_id = id)
    print(project)
    return render(request,'projects/detail_project.html',{
        'project' : project,
        'tasks' : tasks
    })