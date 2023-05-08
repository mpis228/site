from django.contrib.auth.models import AbstractUser
from django.db import models

#абстрактный клас  просто вызиваем
class User(AbstractUser):
    pass #мы с ним ничего не делаем по другому не будет работать все что связано с пользованелями

class Post(models.Model):
    """даные поста"""
    author = models.CharField('автор', max_length=154)
    title = models.CharField('заголовок', max_length=254)
    content = models.TextField('Текст')
    time_create = models.DateTimeField('Время Создания')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.author}: {self.title}'
