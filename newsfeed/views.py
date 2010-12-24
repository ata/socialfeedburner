from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from socialauth.decorators import need_profile
from socialauth.utils import twitter
from socialauth.models import *
from oauth import oauth

@need_profile
def index(request):
    #t = TwitterUserProfile.objects.get()
    #token = oauth.OAuthToken.from_string(t.oauth_token)
    #news = twitter.api('http://api.twitter.com/1/statuses/friends_timeline.json',token)
    return render_to_response('newsfeed/index.html',{'user': request.user})

@need_profile
def newest(request):
    return HttpResponse('index')
    
@need_profile
def older(request):
    return HttpResponse('index')
