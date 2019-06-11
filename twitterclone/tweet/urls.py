from django.contrib.auth.decorators import login_required
from django.urls import path
from twitterclone.tweet.views import (CreateTweetView, TweetView)


urlpatterns = [
    path('tweet/', login_required(CreateTweetView.as_view()),
         name='createtweet'),
    path('tweet/<int:id>/', TweetView.as_view(), name='specific')
]
