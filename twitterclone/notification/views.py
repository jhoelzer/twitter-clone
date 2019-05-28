from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from twitterclone.notification.models import Notification
from twitterclone.twitteruser.models import TwitterUser


@login_required()
def notification_view(request):
    html = '../templates/notifications.html'
    current = TwitterUser.objects.filter(user=request.user).first()
    notifications = Notification.objects.filter(username=current)

    for notify in notifications:
        notify.delete()

    return render(request, html, {'notifications': notifications})
