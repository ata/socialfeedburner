from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from oauth import oauth
from socialauth.utils import twitter
from socialauth.models import *

def index(request):
    return HttpResponse('Index connection')
    
def profile(request):
    try:
        form = UserCreationForm(instance=request.user)
    except:
        user = User.objects.get(id=request.session['user_id'])
        form = UserCreationForm(instance=user)
    if request.method == 'POST':
        if form.validate():
            form.save()
    return render_to_response('socialauth/profile.html', {'form': form ,})

def twitter_connect(request):
    try:
       token = twitter.get_unauthorized_token()
    except:
        return render_to_response('socialauth/twitter_connect_error.html')
    request.session['token'] = token.to_string()
    return HttpResponseRedirect(twitter.get_authorization_url(token))
    

def twitter_connect_done(request):
    token = request.session.get('token', None)
    if not token:
        return render_to_response('socialauth/twitter_connect_error.html', {'token': True})
    token = oauth.OAuthToken.from_string(token)
    if token.key != request.GET.get('oauth_token', 'no-token'):
        return render_to_response('socialauth/twitter_connect_error.html', {'mismatch': True})
    token = twitter.get_authorized_token(token)

    # Actually login
    obj = twitter.is_authorized(token)
    if obj is None:
        return render_to_response('socialauth/twitter_connect_error.html', {'username': True})
    try: 
        twitter_profile = TwitterUserProfile.objects.get(\
                  screen_name=obj['screen_name'])
    except: 
        twitter_profile = TwitterUserProfile(screen_name=obj['screen_name'])
    
    twitter_profile.oauth_token = request.session['token']
    twitter_profile.oauth_token_key = token.key
    twitter_profile.oauth_token_secret = token.secret
    twitter_profile.save()
    request.session['user_id'] = twitter_profile.user.id
    del request.session['token']
    
    return HttpResponseRedirect(reverse('newsfeed'))

    
def facebook_connect(request):
    pass
    
def facebook_connect_done(request):
    pass
