from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import MakeTweet
import re
from twitterclone.notification.models import notification
from twitterclone.twitteruser.models import TwitterUser


def view_tweet(request, id):
    html = 'tweet.html'
    data = Tweet.objects.filter(id=id)
    return render(request, html, {'data': data})


@login_required
def viewhomepage(request):
    html = 'index.html'
    following = request.user.twitteruser.following.all()
    data = Tweet.objects.filter(
        tweet_author__in=following).order_by('-post_date')
    return render(request, html, {'data': data})


@login_required
def make_tweets(request):
    html = 'add_tweet.html'
    if request.method == 'POST':
        form = MakeTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                tweet_author=request.user.twitteruser,
                body=data['body']
            )
            if '@' in data['body']:
                usernames = re.findall(r'@(\w+)', data['body'])
                for username in usernames:
                    twitteruser = TwitterUser.objects.get(
                        user__username=username)
                    notification.objects.create(
                        tweet=tweet,
                        twitter_user=twitteruser
                    )
        return HttpResponseRedirect(reverse('homepage'))
    form = MakeTweet()
    return render(request, html, {'form': form})