from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet



class notification(models.Model):
    user = models.ForeignKey(TwitterUser,
                             on_delete=models.CASCADE,
                             related_name='notification_user'
                             )
    seen = models.BooleanField(default=False)
    notification_total = models.IntegerField(default=0)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.tweet.message} - {self.tweet.user}'