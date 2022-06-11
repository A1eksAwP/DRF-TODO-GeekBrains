from rest_framework.serializers import ModelSerializer
from users.models import MyUserModel

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ['id', 'age', 'username', 'first_name', 'last_name', 'email', 'phone', 'city']

class UserModelSerializerV2(ModelSerializer):
    class Meta:
        model = MyUserModel
        fields = ['id', 'age', 'username', 'first_name', 'last_name', 'email', 'phone', 'city', 'is_superuser', 'is_staff']