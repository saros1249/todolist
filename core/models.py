from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole:
    USER = 'user'
    ADMIN = 'admin'
    choices = (('Пользователь', USER),
               ('Админ', ADMIN),)


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default='user', max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.username

