from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todo.views import ProjectModelViewSet, ProjectUserModelViewSet, ToDoModelViewSet
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt   

schema_view = get_schema_view(
    Info(
        title='Aleksey Shevchuk ToDo Application',
        default_version='0.9',
        description='description',
        contact=Contact(email='send@ashevchuk.ru'),
        license=License(name='MIT')
    ),
    public=True,
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('project_users', ProjectUserModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]