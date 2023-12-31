from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Books(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)
    info = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()
    after = models.CharField(max_length=155)
    number_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.pk)])


class AboutPage(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.title


class QrCode(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    info = models.TextField()
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.title


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_resolved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='reply_to')

    def __str__(self):
        return f'{self.user.username}: {self.text}'

