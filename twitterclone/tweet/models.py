from django.db import models
from django.utils import timezone
from twitterclone.twitteruser.models import TwitterUser


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
