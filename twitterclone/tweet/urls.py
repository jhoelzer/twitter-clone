from django.urls import path
from twitterclone.tweet.views import (create_tweet, tweet_view)


urlpatterns = [
    path('tweet/', create_tweet),
    path('tweet/<int:id>/', tweet_view, name='specific')
]
