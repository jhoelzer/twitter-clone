import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.notification.models import Notification
from twitterclone.tweet.forms import TweetForm
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


@login_required()
def create_tweet(request):
    form = None
    html = '../templates/main.html'
    header = "What's up?"
    button_val = 'Post'

    if request.method == 'POST':
        form = TweetForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                user=request.user.twitteruser,
                tweet=data['tweet']
            )
            user_match = re.findall(r'@(\w+)', data['tweet'])

            for match in user_match:
                Notification.objects.create(
                    username=TwitterUser.objects.filter(
                        username=match).first(),
                    tweet=tweet
                )

        return HttpResponseRedirect(reverse('home'))

    else:
        form = TweetForm()

    return render(request, html, {'header': header, 'form': form,
                                  'button_val': button_val})


def tweet_view(request, id):
    html = 'tweets.html'
    tweets = Tweet.objects.filter(id=id)
    return render(request, html, {'tweets': tweets})
