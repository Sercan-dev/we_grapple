from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('webpage:post', kwargs={'id': self.id})
