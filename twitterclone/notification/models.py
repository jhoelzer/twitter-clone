from django.db import models
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


class Notification(models.Model):
    username = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE
    )
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f'@{self.username.username} tweeted: {self.tweet.tweet}'
