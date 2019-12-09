from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import notification
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.forms import MakeTweet
from django.contrib.auth.decorators import login_required
import re


@login_required
def viewmainpage(request):
    html = 'tweet/index.html'
    notif = notification.objects.filter(user=request.user.twitteruser).count()
    follow = list(request.user.twitteruser.follow.all())
    tweet = []
    for followee in follow:
        tweet += Tweet.objects.filter(user=followee)
    tweet = sorted(tweet, key=lambda tweet: tweet.post_time, reverse=True)
    return render(request, html, {
        'tweet': tweet, 'notif': notif})
 

@login_required
def maketweet(request):
    html = 'tweet/tweet_form.html'
    if request.method == 'POST':
        form = MakeTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                user=request.user.twitteruser,
                message=data['message']
            )
            reggie = re.findall(r'@(\w+)', data['message'])
            if reggie:
                for item in reggie:
                    try:
                        user_check = TwitterUser.objects.get(username=item)
                    except TwitterUser.DoesNotExist:
                        user_check = None
                    if user_check:
                        notification.objects.create(
                            user=user_check,
                            tweet=new_tweet
                        )
            return HttpResponseRedirect(reverse('homepage'))

    form = MakeTweet()
    return render(request, html, {'form': form})


def viewtweet(request, id):
    html = 'tweet/view_tweet.html'
    data = Tweet.objects.filter(id=id)
    return render(request, html, {'data': data})


# stretch goal
def edittweet(request, id):
    pass