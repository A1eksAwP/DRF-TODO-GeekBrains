from rest_framework.viewsets import ModelViewSet
from .models import MyUserModel
from users.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = MyUserModel.objects.all()
    serializer_class = UserModelSerializer