import time
import datetime
from django.db import models
from django.contrib.auth.models import User
from socialauth.models import *

#class TwitterNewsFeed(models.Model):
    #"""
    #news feed from twitter account
    #"""
    #content = models.CharField(max_length=140)
    #datetime = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, related_name='posts')
    #profile = models.ForeignKey(TwitterUserProfile, \
                                #related_name='news_feeds')
    #@classmethod
    #def count_after(cls, user, after):
        #"""
        #counting newsfeed user after params 'after' time, 
        #'after' param is string timestamp
        #"""
        #after_date = datetime.datetime.fromtimestamp(float(after))
        #return cls.objects.filter(datetime__gt=after).count()

#class FacebookNewsFeed(models.Model):
    #"""
    #news feed from facebook account
    #"""
    #content = models.CharField(max_length=500)
    #datetime = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey(User, related_name='posts')
    #profile = models.ForeignKey(FacebookUserProfile, \
                                #related_name='news_feeds')
    

