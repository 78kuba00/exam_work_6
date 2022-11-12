from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='-', verbose_name='Автор')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Почта')
    message = models.TextField(max_length=1000,  null=False, blank=False, verbose_name='Запись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.author}'