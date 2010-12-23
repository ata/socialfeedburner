from django.db import models
from django.contrib.auth.models import User


class TwitterUserProfile(models.Model):
    """
    For users who login via Twitter.
    """
    screen_name = models.CharField(max_length=200, unique=True, db_index=True)
    user = models.ForeignKey(User, related_name='twitter_profiles')
    access_token = models.CharField(max_length=255, blank=True, null=True, editable=False)
    profile_image_url = models.URLField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=160, blank=True, null=True)

    def __unicode__(self):
        return "%s's profile" % self.user
        

class FacebookUserProfile(models.Model):
    """
    For users who login via Facebook.
    """
    facebook_uid = models.CharField(max_length=20, unique=True, db_index=True)
    user = models.ForeignKey(User, related_name='facebook_profiles')
    profile_image_url = models.URLField(blank=True, null=True)
    profile_image_url_big = models.URLField(blank=True, null=True)
    profile_image_url_small = models.URLField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    about_me = models.CharField(max_length=160, blank=True, null=True)
    
    def __unicode__(self):
        return "%s's profile" % self.user


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

class TwitterNewsFeed(NewsFeed):
    """
    news feed from twitter account
    """
    twitter_profile = models.ForeignKey(TwitterUserProfile, related_name='news_feeds')

class FacebookNewsFeed(NewsFeed):
    """
    news feed from facebook account
    """
    twitter_profile = models.ForeignKey(FacebookUserProfile, related_name='news_feeds')
    

