from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


def viewprofile(request, id):
    html = 'twitteruser/userprofile.html'
    twitteruser= TwitterUser.objects.filter(id=id).first()
    tweet = Tweet.objects.filter(user=twitteruser).order_by('-post_time')
    return render(request, html, {
        'tweet': tweet, 'twitteruser': twitteruser})


def followuser(request, id):
    followuser = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.add(followuser)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))


def unfollowuser(request, id):
    followuser = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.remove(followuser)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))