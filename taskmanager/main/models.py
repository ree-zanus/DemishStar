from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    text = models.TextField('Полное описание')
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Clients(models.Model):
    name = models.CharField('Имя', max_length=50)
    SurName = models.CharField('Фамилия', max_length=50)
    Patronymic = models.CharField('Отчество', max_length=50)
    Number = models.CharField('Номер', max_length=50)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'