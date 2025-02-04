from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    # retorna el nombre, en vez de "objet()"
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE) #esto hace que se gener ENTITY_ID_ID, no poner _id.
    
    def __str__(self):
        return self.title
    
# corrigiendo esa vaina
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Sin _id

    def __str__(self):
        return self.title