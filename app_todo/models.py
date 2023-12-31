from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=255, verbose_name='Todo title')
    description = models.TextField(verbose_name='Full text todo')
    start_time = models.DateField(verbose_name='Start time')
    end_time = models.DateField(verbose_name='End time')
    statuses = {
        ('a', 'active'),
        ('d', 'done'),
        ('n', 'not yet'),
        ('b', 'bad boy'),
        ('a', 'always good'),
        ('i', 'interestingly'),
        ('r', 'responsibility')
    }
    status = models.CharField(max_length=15, verbose_name='Status', choices=statuses)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo_list'
        ordering = ['start_time', 'title']

    # def get_absolute_url(self):
        # return reverse('users', args=[str(self.id)])
