from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    username = models.CharField(max_length=50)
    display = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.user.username
