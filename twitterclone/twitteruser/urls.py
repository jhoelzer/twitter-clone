from django.urls import path
from twitterclone.twitteruser.views import (
    signup_user, profile_view, is_following_view)


urlpatterns = [
    path('signup/', signup_user),
    path('<str:username>/', profile_view),
    path('followstat/<str:username>/', is_following_view)
]
