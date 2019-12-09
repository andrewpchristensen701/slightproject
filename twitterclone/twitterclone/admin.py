from django.contrib import admin
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import notification

admin.site.register(TwitterUser)
admin.site.register(Tweet)
admin.site.register(notification)