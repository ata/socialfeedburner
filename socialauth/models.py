from django.db import models
from django.contrib.auth.models import User
from oauth.oauth import OAuthToken

__all__ = ('UserProfile','TwitterUserProfile','FacebookUserProfile')

class UserProfile(models.Model):
    """
    User Profile
    """
    user = models.OneToOneField(User,related_name='profile')
    
    def __unicode__(self):
        return "%s's profile" % self.user
    
    def has_facebook_connected(self):
        try:
            self.user.facebook_profiles
            return True
        except:
            return False
            
    def has_twitter_connected(self):
        #return self.user.twitter_profiles.count() > 0
        try:
            self.user.twitter_profiles
            return True
        except:
            return False
    
    def has_connected(self):
        return self.has_twitter_connected() or self.has_facebook_connected()
        

class TwitterUserProfile(models.Model):
    """
    For users who login via Twitter.
    """
    screen_name = models.CharField(max_length=200, unique=True, db_index=True)
    user = models.OneToOneField(User, related_name='twitter_profiles')
    oauth_token = models.CharField(max_length=500, blank=True, null=True)
    oauth_token_key = models.CharField(max_length=255, blank=True, null=True)
    oauth_token_secret = models.CharField(max_length=255, blank=True, \
                                    null=True)
    profile_image_url = models.URLField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=160, blank=True, null=True)

    def __unicode__(self):
        return "%s's profile" % self.user
        
    def get_token(self):
        return OAuthToken(self.oauth_token_key, self.oauth_token_secret)
        

class FacebookUserProfile(models.Model):
    """
    For users who login via Facebook.
    """
    facebook_uid = models.CharField(max_length=20, unique=True, db_index=True)
    user = models.OneToOneField(User, related_name='facebook_profiles')
    profile_image_url = models.URLField(blank=True, null=True)
    profile_image_url_big = models.URLField(blank=True, null=True)
    profile_image_url_small = models.URLField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    about_me = models.CharField(max_length=160, blank=True, null=True)
    
    def __unicode__(self):
        return "%s's profile" % self.user
