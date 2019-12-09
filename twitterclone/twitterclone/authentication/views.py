from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitterclone.authentication.forms import LoginForm, UserAdd
from twitterclone.twitteruser.models import TwitterUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def loginview(request):
    html = 'authentication/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_view'))


def createuser(request):
    html = 'authentication/signup.html'
    if request.method == 'POST':
        form = UserAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            new_user = TwitterUser.objects.create(
                user=user,
                username=data['username'],
                password=data['password'],
                bio=data['bio'],
            )
            new_user.follow.add(new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = UserAdd()
    return render(request, html, {'form': form})