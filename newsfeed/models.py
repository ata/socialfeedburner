import time
import datetime
from django.db import models
from django.contrib.auth.models import User
from socialauth.models import *

class NewsFeed(models.Model):
    """
    news feed from all social media
    """
    content = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='posts')
    
    def __unicode__(self):
        return self.content
    
    @classmethod
    def count_after(cls, user, after):
        """
        counting newsfeed user after params 'after' time, 
        'after' param is string timestamp
        """
        after_date = datetime.datetime.fromtimestamp(float(after))
        return cls.objects.filter(datetime__gt=after).count()

class TwitterNewsFeed(NewsFeed):
    """
    news feed from twitter account
    """
    profile = models.ForeignKey(TwitterUserProfile, \
                                related_name='news_feeds')

class FacebookNewsFeed(NewsFeed):
    """
    news feed from facebook account
    """
    profile = models.ForeignKey(FacebookUserProfile, \
                                related_name='news_feeds')
    

