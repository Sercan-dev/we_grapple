from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.dateformat import format


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    published = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    image_url = models.URLField(default="")
    content = models.CharField(max_length=30000)
    draft = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp', '-updated']
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def unix_time(self):
        return format(self.updated, 'U')


class LastUpdate(models.Model):
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def unix_time(self):
        return format(self.updated, 'U')

    def __str__(self):
        return self.unix_time()


class Photo(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(blank=False, null=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


