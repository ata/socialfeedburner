from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from oauth import oauth
from socialauth.utils import *
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
    #if request.user: 
    #    return HttpResponseRedirect(reverse('newsfeed'))
    token = get_unauthorized_token()
    request.session['token'] = token.to_string()
    return HttpResponseRedirect(get_authorization_url(token))

def twitter_connect_done(request):
    token = request.session.get('token', None)
    if not token:
        return render_to_response('callback.html', {'token': True})
    token = oauth.OAuthToken.from_string(token)
    if token.key != request.GET.get('oauth_token', 'no-token'):
        return render_to_response('socialauth/twitter_connect_done.html', {'mismatch': True})
    token = get_authorized_token(token)

    # Actually login
    obj = is_authorized(token)
    if obj is None:
        return render_to_response('socialauth/twitter_connect_done.html', {'username': True})
    try: 
        twitter = TwitterUserProfile.objects.get(\
                  screen_name=obj['screen_name'])
    except: 
        twitter = TwitterUserProfile(screen_name=obj['screen_name'])
    
    twitter.oauth_token = token.key
    twitter.oauth_token_secret = token.secret
    twitter.save()
    request.session['user_id'] = twitter.user.id
    del request.session['token']
    
    return HttpResponseRedirect(reverse('socialauth_profile'))

    
def facebook_connect(request):
    pass
    
def facebook_connect_done(request):
    pass
