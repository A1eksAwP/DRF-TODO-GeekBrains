from rest_framework import permissions

#Класс на основе бэйс, который позволяет изменятиь проект только его создателю
class ProjectOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user