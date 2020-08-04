# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    author = models.CharField('Автор', max_length=250, default='admin')
    text = models.TextField(("Текс"))
    create_date = models.DateTimeField(("Дата создания"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = u'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return '{} {}'.format(self.title, self.create_date)
    