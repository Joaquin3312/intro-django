from django import forms
from myapp.models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Titulo de tarea",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add title'})
    )
    description = forms.CharField(
        label="Descripción de la tarea",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add description'})
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        label="Proyecto",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class CreateNewProject(forms.Form):
    name = forms.CharField(
        label="Ingresa el nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add project name'})
    )