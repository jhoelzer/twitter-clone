from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        html = 'home.html'
        current = TwitterUser.objects.get(user=request.user)
        user_tweets = Tweet.objects.filter(user=request.user.twitteruser)
        followers = current.follow.all()
        follow_tweets = Tweet.objects.filter(user__in=followers)
        tweets = (follow_tweets | user_tweets).distinct().order_by('-date')
        return render(request, html, {'tweets': tweets})
