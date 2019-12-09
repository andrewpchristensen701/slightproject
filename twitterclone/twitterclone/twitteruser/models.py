from django.db import models
from django.contrib.auth.models import User
from twitterclone.tweet.models import Tweet


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    bio = models.CharField(max_length=200, blank=True, null=True)
    follow = models.ManyToManyField('self',
                                    symmetrical=False,
                                    blank=True
                                    )
    def __str__(self):
        return f'{self.username}'