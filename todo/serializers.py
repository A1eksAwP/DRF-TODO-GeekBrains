from rest_framework.serializers import ModelSerializer
from rest_framework.relations import StringRelatedField
from todo.models import Project, ProjectUser, TODO



class ProjectSerializer(ModelSerializer):
    project = StringRelatedField(many=True)
    # tasks = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectUserSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ProjectUser
        fields = '__all__'


class TODOSerializer(ModelSerializer):
    
    project = StringRelatedField()
    creator = StringRelatedField()
    users = ProjectUserSerializer(many=True)

    class Meta:
        model = TODO
        fields = '__all__'