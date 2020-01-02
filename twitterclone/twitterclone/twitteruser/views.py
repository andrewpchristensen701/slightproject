from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import notification


@login_required
def NewUserForm_view(request):
    html = 'NewUser.html'
    user = request.user
    twitteruser = TwitterUser.objects.get(user=user)
    notifications = notification.objects.filter(
        viewed=twitteruser, not_viewed=True)
    number_of_notifications = len(notifications)
    followed = twitteruser.following.all()
    tweets = Tweet.objects.filter(author__in=followed).ordered_by(
        '-post_date')

    number_following = len(followed)
    return render(request, html, {
        'twitteruser': twitteruser,
        'number_following': number_following,
        'followed': followed,
        'tweets': tweets,
        'number_of_notifications': number_of_notifications
    })


def profile_view(request, id):
    html = 'user_profile.html'
    twitteruser = TwitterUser.objects.filter(id=id).first()
    tweets = Tweet.objects.filter(
        tweet_author=twitteruser).order_by('-post_date')
    return render(
        request, html, {
            'tweets': tweets,
            'twitteruser': twitteruser,
            'is_followed': True
        }
    )


def follow_user(request, id):
    follow_user = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.add(follow_user)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))


def unfollow_user(request, id):
    unfollow_user = TwitterUser.objects.get(id=id)
    request.user.twitteruser.follow.remove(unfollow_user)
    return HttpResponseRedirect(reverse('profile_view', kwargs={'id': id}))