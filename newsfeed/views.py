from django.utils import simplejson as json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from newsfeed.utils import get_default_posts, get_older_posts

@login_required
def index(request):
    return render_to_response('newsfeed/index.html',{'user': request.user})

@login_required
def firstload(request):
    posts = get_default_posts(request.user)
    return HttpResponse(json.dumps(posts), mimetype='application/json')

@login_required
def newest(request, since_id):
    posts = get_newest_posts(request.user, since_id)
    return HttpResponse(json.dumps(posts), mimetype='application/json')
    
@login_required
def older(request, max_id):
    posts = get_older_posts(request.user, max_id)
    return HttpResponse(json.dumps(posts), mimetype='application/json')
