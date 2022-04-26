from rest_framework.viewsets import ModelViewSet
from .permissions import ProjectOwnerOrReadOnly
from .filters import ProjectContainsFilter
from .models import Project, ProjectUser, ToDo
from .serializers import ProjectUserSerializer, ProjectSerializer, ToDoSerializer
from rest_framework.mixins import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, \
    BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filterset_class = ProjectContainsFilter
    permission_classes = (ProjectOwnerOrReadOnly, )


class ProjectUserModelViewSet(ModelViewSet):
    serializer_class = ProjectUserSerializer
    queryset = ProjectUser.objects.all()


class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    filterset_fields = ['project', 'created', 'deadline']

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

# class ProjectOwnerPermission(DjangoModelPermissions):

#     def has_object_permission(self, request, view, obj):
#         if request.user.username in obj.objects.all():
#             return super().has_permission(request, view)
#         else:
#             return False