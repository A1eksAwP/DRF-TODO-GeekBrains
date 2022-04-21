from django.contrib import admin
from todo.models import TODO, Project, ProjectUser


admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(TODO)