from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    NickName = models.CharField('Кличка', max_length=50)
    Father = models.CharField('Отец', max_length=50)
    Mother = models.CharField('Мать', max_length=50)
    Sex = models.CharField('Пол', max_length=10)
    Color = models.CharField('Окрас', max_length=15)
    Data = models.CharField('Дата рождения', max_length=15)
    Text = models.TextField('Описание', max_length=255)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Clients(models.Model):
    SurName = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    Patronymic = models.CharField('Отчество', max_length=50)
    Number = models.CharField('Номер', max_length=10)
    Comment = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'