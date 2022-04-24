from django.utils import timezone
from django.db import models
from users.models import MyUserModel


class Project(models.Model): #Проект
    name = models.CharField(verbose_name='Название проекта', unique=True, max_length=80)
    repository_url = models.URLField(verbose_name='Репозиторий', blank=True, max_length=200)
    creator = models.ForeignKey(MyUserModel, verbose_name='Авторыы', related_name='creator', null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    def __str__(self):
        return self.name


class ProjectUser(models.Model): #Пользователь проекта
    user = models.ForeignKey(MyUserModel, verbose_name='Пользователь', related_name='user', on_delete=models.CASCADE,)
    project = models.ForeignKey(Project, verbose_name='Проект', related_name='project', on_delete=models.CASCADE)

    def __str__(self):
        return f'Пользователь {self.user} занимается задачей: {self.project}'


class ToDo(models.Model): #Задача, стоящая перед пользователями
    project = models.ForeignKey(Project, verbose_name='Проект', related_name='ToDo', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='Описание задачи', blank=True)
    created_by = models.ForeignKey(MyUserModel, verbose_name='Автор', related_name='created_by', null=True, blank=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(ProjectUser, verbose_name='Пользователи', blank=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    deadline = models.DateField(verbose_name='Дэдлайн', blank=True)

    def save(self, *args, **kwargs):
        super(ToDo, self).save(*args, **kwargs)

    def __str__(self):
        return self.description