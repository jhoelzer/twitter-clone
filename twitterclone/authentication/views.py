from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from twitterclone.authentication.forms import LoginForm


def login_user(request):
    form = None
    html = '../templates/main.html'
    header = 'Login'
    button_val = 'Login'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    else:
        form = LoginForm()

    return render(request, html, {'header': header, 'form': form,
                                  'button_val': button_val})


def logout_user(request):
    html = 'logout.html'
    logout(request)
    return render(request, html)
