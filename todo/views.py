from rest_framework.viewsets import ModelViewSet
from .filters import ProjectContainsFilter
from .models import Project, ProjectUser, ToDo
from .serializers import ProjectUserSerializer, ProjectSerializer, ToDoSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import *


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectContainsFilter


class ProjectUserModelViewSet(ModelViewSet):
    serializer_class = ProjectUserSerializer
    queryset = ProjectUser.objects.all()


class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['project', 'created', 'deadline']

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()