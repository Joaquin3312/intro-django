from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about',views.about, name="about"),
    path('hello/<str:username>',views.hello, name="hello"),
    
    # PROJECTS
    path('projects/',views.projects, name="projects"),
    path('edit_project/<int:id>',views.edit_project, name="edit_project"),
    path('projects/<int:id>',views.detail_project, name="detail_project"),
    path('delete_project/<int:id>',views.delete_project, name="delete_project"),
    path('create_project/',views.create_project, name="create_project"),
    
    # TASKS
    path('tasks/',views.tasks, name="tasks"),
    path('create_tasks/',views.create_task, name="create_tasks"),
    path('delete_task/<int:id>',views.delete_task, name="delete_task"),
    path('edit_task/<int:id>',views.edit_task, name="edit_task"),
    path('complete_task/<int:id>',views.complete_task, name="complete_task"),
     
]