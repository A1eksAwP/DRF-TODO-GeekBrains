from rest_framework.serializers import ModelSerializer
from rest_framework.relations import StringRelatedField
from todo.models import Project, ProjectUser, ToDo
from rest_framework import serializers


class ProjectSerializer(ModelSerializer):

    #Сделал это поле неизменяемым, чтобы залогенинный пользователь на сайте и был непосредственно автором
    creator = serializers.HiddenField(default = serializers.CurrentUserDefault())

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

    created_by = serializers.HiddenField(default = serializers.CurrentUserDefault())
    
    class Meta:
        model = ToDo
        fields = '__all__'