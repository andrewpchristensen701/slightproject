from django.db import models
from django.utils import timezone
# from twitterclone.twitteruser.models import TwitterUser


class Tweet(models.Model):
    user = models.ForeignKey(
        'twitterclone.TwitterUser',
        on_delete=models.CASCADE,
        related_name='tweeter')
    message = models.TextField(max_length=140)
    post_time = models.DateTimeField(default=timezone.now)