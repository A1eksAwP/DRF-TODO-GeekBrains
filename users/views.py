from .models import MyUserModel
from users.serializers import UserModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet

class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = MyUserModel.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]