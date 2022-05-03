import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate, APITestCase
from .views import ProjectModelViewSet
from .models import Project, ToDo
from users.models import MyUserModel as User
from mixer.backend.django import mixer


class TestProjectApi(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='TestUser', password='test')
        self.project = Project.objects.create(name='Новый пустой проект')

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/projects/')
        force_authenticate(request, self.user)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TestProjectApiClient(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='TestUser', password='test')
        self.project = Project.objects.create(name='Новый пустой проект') 

    def test_get_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_2(self):
        self.client.login(username='TestUser', password='test')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()

    def test_post_project(self):
        self.client.login(username='TestUser', password='test')
        response = self.client.post('/projects/', data={
            'name': 'Супер проект',
            'repository_url': 'https://github.com/A1eksAwP/special',
            'is_active': False,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get(pk=response.data.get('id'))
        self.assertEqual(project.name, 'Супер проект')


class TestProjectApiClient2(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='TestUser2', password='test')
        self.project = mixer.blend(Project, name='Автоматически созданный проект')
        # self.todo = mixer.blend(ToDo, project__name = 'Автоматически созданный проект')

    def test_get_list(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_2(self):
        self.client.login(username='TestUser2', password='test')
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()

    def test_post_project(self):
        self.client.login(username='TestUser2', password='test')
        response = self.client.post('/projects/', data={
            'name': 'Супер проект с APITestCase',
            'repository_url': 'https://github.com/A1eksAwP/special',
            'is_active': False,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get(pk=response.data.get('id'))
        self.assertEqual(project.name, 'Супер проект с APITestCase')

    def test_get_auto_todo(self):
        todo = mixer.blend(ToDo, project__name = 'Автоматически созданный проект 2')
        response = self.client.get(f'/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)