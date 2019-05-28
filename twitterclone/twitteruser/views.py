from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.forms import SignupForm
from twitterclone.twitteruser.models import TwitterUser


def signup_user(request):
    form = None
    html = '../templates/main.html'
    header = 'Signup'
    button_val = 'Signup'

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password']
            )
            login(request, user)
            TwitterUser.objects.create(
                username=data['username'],
                display=data['display'],
                user=user
            )
            return HttpResponseRedirect(reverse('home'))

    else:
        form = SignupForm()

    return render(request, html, {'header': header, 'form': form,
                                  'button_val': button_val})


def profile_view(request, username):
    html = '../templates/twitteruser.html'
    target_user = TwitterUser.objects.filter(username=username).first()
    target_tweets = Tweet.objects.filter(user=target_user).order_by('-date')
    num_tweet = len(target_tweets)
    num_followers = target_user.follow.count
    follow_stat_button = None

    data = {}

    if request.user.is_authenticated:
        current = TwitterUser.objects.filter(
            username=request.user.twitteruser).first()
        notifications = Notification.objects.filter(username=current).count

        if target_user not in request.user.twitteruser.follow.get_queryset():
            follow_stat_button = 'Follow'

        else:
            follow_stat_button = 'Unfollow'

        data = {'target_user': target_user,
                'notifications': notifications,
                'tweets': target_tweets,
                'num_tweet': num_tweet,
                'follow_stat_button': follow_stat_button,
                'num_followers': num_followers}

    else:
        data = {'target_user': target_user,
                'tweets': target_tweets,
                'num_tweet': num_tweet,
                'num_followers': num_followers}

    return render(request, html, data)


def is_following_view(request, username):
    html = '../templates/followstat.html'
    is_following = False
    header = "Following"
    target_user = TwitterUser.objects.filter(username=username).first()
    current = request.user.twitteruser
    if target_user not in current.follow.get_queryset():
        current.follow.add(target_user)
        is_following = True

    else:
        current.follow.remove(target_user)
        is_following = False

    current.save()
    return render(request, html, {'header': header,
                                  'is_following': is_following})
