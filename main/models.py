from tabnanny import verbose
from django.db import models


class NameForm(models.Model):
    name = models.CharField('name', max_length=5)
    author = models.CharField('author', max_length=5)
    number = models.CharField('number', max_length=5)

    class Meta:
        verbose_name = 'book'

