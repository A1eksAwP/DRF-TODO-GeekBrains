from django.contrib import admin
from todo.models import ToDo, Project, ProjectUser


admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(ToDo)