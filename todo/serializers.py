from rest_framework.serializers import ModelSerializer
from rest_framework.relations import StringRelatedField
from todo.models import Project, ProjectUser, ToDo


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectUserSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ProjectUser
        fields = '__all__'


class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'