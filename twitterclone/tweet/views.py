import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views import View
from twitterclone.notification.models import Notification
from twitterclone.tweet.forms import TweetForm
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


class CreateTweetView(View):
    model = Tweet
    form_class = TweetForm
    template_name = '../templates/main.html'
    header = "What's up?"
    button_val = 'Post'
    url_redirect = 'home'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      {'header': self.header, 'form': form,
                       'button_val': self.button_val})

    def post(self, request):
        form = self.form_class(request.POST)

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

            return HttpResponseRedirect(reverse(self.url_redirect))

        return render(request, self.template_name,
                      {'header': self.header, 'form': form,
                       'button_val': self.button_val})


class TweetView(View):
    def get(self, request, id):
        html = 'tweets.html'
        tweets = Tweet.objects.filter(id=id)
        return render(request, html, {'tweets': tweets})
