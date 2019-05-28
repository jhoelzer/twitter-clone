from twitterclone.authentication.views import (login_user, logout_user)
from django.urls import path

urlpatterns = [
    path('login/', login_user),
    path('logout/', logout_user)
]