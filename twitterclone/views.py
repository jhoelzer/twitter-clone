from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


@login_required()
def home_view(request):
    html = 'home.html'
    current = TwitterUser.objects.get(user=request.user)
    user_tweets = Tweet.objects.filter(user=request.user.twitteruser)
    followers = current.follow.all()
    follow_tweets = Tweet.objects.filter(user__in=followers)
    tweets = (follow_tweets | user_tweets).distinct().order_by('-date')
    return render(request, html, {'tweets': tweets})
