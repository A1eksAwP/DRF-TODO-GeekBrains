from .models import MyUserModel
from users.serializers import UserModelSerializer, UserModelSerializerV2
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = MyUserModel.objects.all()
    vers = {
        '2.0': UserModelSerializerV2
    }

    def get_serializer_class(self):
        return self.vers.get(self.request.version, UserModelSerializer)

    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]