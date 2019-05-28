from django import forms
# from twitteruser.authentication.models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
