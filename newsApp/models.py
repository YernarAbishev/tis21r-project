from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255) # varchar
    content = models.TextField("Контент")
    source = models.CharField("Источник", max_length=50)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"